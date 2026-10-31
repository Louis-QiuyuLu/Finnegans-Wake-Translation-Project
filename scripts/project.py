#!/usr/bin/env python3
"""Validate the manuscript and export Markdown, a static reader, and EPUB 3."""

import argparse
from collections import Counter
from html import escape
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import shutil
import sys
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path(__file__).resolve().parents[1]
KINDS = {"wordplay": "双关", "culture": "文化", "allusion": "典故", "sound": "声音", "structure": "结构", "syntax": "句法", "translation": "译法"}
CERTAINTY = {"supported": "据来源", "proposal": "译者判断", "uncertain": "存疑"}
STATUS = {"draft": "试译", "revised": "修订待审", "reviewed": "已审校"}
COVERAGE = {"not_started": "待译", "partial": "部分试译", "complete": "整章录入"}


def load_project(root=ROOT):
    read = lambda path: json.loads(path.read_text(encoding="utf-8"))
    chapters = [read(p) for p in (root / "manuscript/chapters").glob("*.json")]
    chapters.sort(key=lambda c: (c["pages"][0], c["number"]))
    data = {"config": read(root / "book.config.json"), "chapters": chapters,
            "sources": read(root / "sources/catalog.json"), "glossary": read(root / "glossary/terms.json")}
    if (root / "progress/checkpoint.json").exists():
        data["checkpoint"] = read(root / "progress/checkpoint.json")
    return data


def validate(data):
    errors = []
    sources = data["sources"]
    source_ids = {s.get("id") for s in sources}
    for sid, count in Counter(s.get("id") for s in sources).items():
        if not sid or count > 1:
            errors.append(f"duplicate or empty source: {sid}")
    for source in sources:
        if urlsplit(source.get("url", "")).scheme not in ("https", "http"):
            errors.append(f"invalid source URL: {source.get('id')}")
    seen_segments, seen_notes, seen_chapters = set(), set(), set()

    def require_text(record, keys, context):
        for key in keys:
            if not isinstance(record.get(key), str) or not record[key].strip():
                errors.append(f"empty {key}: {context}")

    def check_sources(ids, context):
        if not isinstance(ids, list) or not ids:
            errors.append(f"missing source: {context}")
        else:
            for sid in ids:
                if sid not in source_ids:
                    errors.append(f"unknown source {sid}: {context}")

    for chapter in data["chapters"]:
        cid = chapter.get("id", "")
        if not re.fullmatch(r"(?:I\.[1-8]|II\.[1-4]|III\.[1-4]|IV)", cid) or cid in seen_chapters:
            errors.append(f"invalid or duplicate chapter: {cid}")
        seen_chapters.add(cid)
        pages = chapter.get("pages", [])
        if len(pages) != 2 or not all(type(n) is int and n > 0 for n in pages) or pages[0] > pages[1]:
            errors.append(f"invalid chapter pages: {cid}")
            continue
        coverage = chapter.get("coverage")
        segments = chapter.get("segments", [])
        if coverage not in COVERAGE or (coverage == "not_started" and segments) or (coverage != "not_started" and not segments):
            errors.append(f"coverage inconsistent: {cid}")
        if coverage == "complete" and not chapter.get("coverage_review", "").strip():
            errors.append(f"complete chapter requires coverage reviewer and basis: {cid}")
        previous_end = None
        for segment in segments:
            sid = segment.get("id", "")
            if sid in seen_segments:
                errors.append(f"duplicate segment: {sid}")
            seen_segments.add(sid)
            if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", sid):
                errors.append(f"invalid segment ID: {sid}")
            require_text(segment, ["original", "draft", "translation", "locator"], sid)
            check_sources([segment.get("source_id")], sid)
            position = segment.get("range", [])
            if len(position) != 4 or not all(type(n) is int and n > 0 for n in position):
                errors.append(f"invalid range: {sid}")
            else:
                p1, l1, p2, l2 = position
                if p1 < pages[0] or p2 > pages[1]:
                    errors.append(f"range outside chapter: {sid}")
                if (p1, l1) > (p2, l2):
                    errors.append(f"reversed range: {sid}")
                if previous_end is not None and (p1, l1) <= previous_end:
                    errors.append(f"overlapping or unordered range: {sid}")
                previous_end = (p2, l2)
                expected = f"{p1:03d}.{l1:02d}–{p2:03d}.{l2:02d}"
                if segment.get("locator") != expected:
                    errors.append(f"locator disagrees with range: {sid}; expected {expected}")
            status = segment.get("status")
            if status not in STATUS:
                errors.append(f"invalid status: {sid}")
            reviewers = segment.get("reviewers", [])
            if status == "reviewed" and (not reviewers or not all(isinstance(r, str) and r.strip() for r in reviewers)):
                errors.append(f"reviewed segment requires named reviewer: {sid}")
            for note in segment.get("notes", []):
                nid = note.get("id", "")
                if nid in seen_notes or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", nid):
                    errors.append(f"invalid or duplicate note: {nid}")
                seen_notes.add(nid)
                require_text(note, ["lemma", "text"], nid)
                if note.get("kind") not in KINDS or note.get("certainty") not in CERTAINTY:
                    errors.append(f"invalid note classification: {nid}")
                check_sources(note.get("source_ids"), nid)
            for alternative in segment.get("alternatives", []):
                require_text(alternative, ["text", "reason", "attribution"], sid)
    for term in data.get("glossary", []):
        require_text(term, ["term", "translation", "note"], "glossary")
        check_sources(term.get("source_ids"), term.get("term"))
    checkpoint = data.get("checkpoint")
    if checkpoint:
        chapter = next((c for c in data["chapters"] if c["id"] == checkpoint.get("chapter")), None)
        position = checkpoint.get("next", [])
        if chapter is None or len(position) != 2 or not all(type(n) is int and n > 0 for n in position):
            errors.append("invalid checkpoint chapter or next position")
        elif not chapter["pages"][0] <= position[0] <= chapter["pages"][1]:
            errors.append("checkpoint outside current chapter")
        elif chapter["segments"] and tuple(position) <= tuple(chapter["segments"][-1]["range"][2:]):
            errors.append("checkpoint must follow latest sequential segment")
        require_text(checkpoint, ["next_original", "updated"], "checkpoint")
    return errors


def statistics(data):
    chapters = data["chapters"]
    segments = [s for c in chapters for s in c["segments"]]
    return {"chapters": len(chapters), "started": sum(bool(c["segments"]) for c in chapters),
            "complete": sum(c["coverage"] == "complete" for c in chapters), "segments": len(segments),
            "reviewed": sum(s["status"] == "reviewed" for s in segments),
            "notes": sum(len(s["notes"]) for s in segments)}


def slug(chapter):
    return chapter["id"].replace(".", "-")


def paragraphs(text, css=""):
    attribute = f' class="{css}"' if css else ""
    return "".join(f"<p{attribute}>{escape(p)}</p>" for p in text.split("\n\n"))


def source_links(ids, data, prefix=""):
    by_id = {s["id"]: s for s in data["sources"]}
    return " · ".join(f'<a href="{prefix}sources.html#source-{escape(sid)}">{escape(by_id[sid]["title"])}</a>' for sid in ids)


def render_segments(chapter, data, epub=False):
    if not chapter["segments"]:
        return '<section class="empty"><h2>此章待译</h2><p>目录已建，正文尚未录入。后续将按页行逐段补齐。</p></section>'
    chunks = []
    for segment in chapter["segments"]:
        sid = escape(segment["id"])
        notes = segment["notes"]
        refs = " ".join(f'<a id="ref-{escape(n["id"])}" href="#note-{escape(n["id"])}" class="noteref"'
                        + (' epub:type="noteref" role="doc-noteref"' if epub else '')
                        + f' aria-label="注 {i}：{escape(n["lemma"])}">[{i}]</a>' for i, n in enumerate(notes, 1))
        note_items = []
        for i, note in enumerate(notes, 1):
            nid = escape(note["id"])
            label = f'{KINDS[note["kind"]]} · {CERTAINTY[note["certainty"]]}'
            content = (f'<p><strong>{i}. {escape(note["lemma"])}</strong> <span class="tag">{label}</span></p>'
                       + paragraphs(note["text"]) + '<p class="source-links">来源：'
                       + source_links(note["source_ids"], data, "../")
                       + f' · <a href="#ref-{nid}"' + (' role="doc-backlink"' if epub else '') + '>返回正文</a></p>')
            if epub:
                note_items.append(f'<aside id="note-{nid}" epub:type="footnote" role="doc-footnote">{content}</aside>')
            else:
                note_items.append(f'<details id="note-{nid}" class="annotation"><summary>{i}. {escape(note["lemma"])} <span class="tag">{label}</span></summary>{paragraphs(note["text"])}<p class="source-links">来源：{source_links(note["source_ids"], data, "../")} · <a href="#ref-{nid}">返回正文</a></p></details>')
        alternatives = "".join('<blockquote>' + paragraphs(a["text"]) + '<p class="muted">'
                               + escape(a["attribution"] + "：" + a["reason"]) + '</p></blockquote>' for a in segment["alternatives"])
        editor = ''
        if not epub:
            note_fields = ''.join(f'<label for="edit-{escape(n["id"])}">{escape(n["lemma"])}</label><textarea id="edit-{escape(n["id"])}" class="edit-note" data-note="{escape(n["id"])}" rows="4">{escape(n["text"])}</textarea>' for n in notes)
            editor = (f'<details class="revision-editor" data-segment="{sid}"><summary>修订本段</summary>'
                      + '<p class="muted">修订先存在本机。提交 GitHub 后，公共读本才会更新。</p>'
                      + f'<label for="edit-{sid}">修订译文</label><textarea id="edit-{sid}" class="edit-translation" rows="6">{escape(segment["translation"])}</textarea>'
                      + '<details class="note-editor"><summary>修订译注文字</summary>' + note_fields + '</details>'
                      + '<div class="edit-actions"><button type="button" class="save-revision">保存并预览</button><button type="button" class="discard-revision">清除此段修订</button>'
                      + '<button type="button" class="rebase-revision" hidden>已对照现稿，采用本次修订</button></div><p class="revision-status" role="status"></p></details>')
        chunks.append(f'<section class="segment" id="{sid}"><h2 class="locator">FW {escape(segment["locator"])} <span class="tag">{STATUS[segment["status"]]}</span></h2>'
                      + '<div class="original" lang="en"><h3>原文</h3>' + paragraphs(segment["original"]) + '</div>'
                      + '<div class="translation"><h3>中文试译</h3>' + paragraphs(segment["translation"]) + '</div>'
                      + f'<p class="note-refs">译注 {refs}</p>'
                      + '<div class="notes"><h3>译注与出处</h3>' + ''.join(note_items) + '</div>'
                      + ('<section class="alternatives"><h3>备选译法</h3>' + alternatives + '</section>' if alternatives else '') + editor
                      + '</section>')
    if chapter["id"] == "IV" and any(c["id"] == "I.1" for c in data["chapters"]):
        chunks.append('<p class="loop"><a href="I-1.' + ('xhtml' if epub else 'html') + '#fw-i1-003-01">回到 003.01，接读开篇 →</a></p>')
    return ''.join(chunks)


def render_sources(data):
    return '<h1>底本与参考资料</h1><p>页行沿用通行版坐标。原著、版本见证、研究意见与社区释义分别标记。</p>' + ''.join(
        f'<section class="source-entry" id="source-{escape(s["id"])}"><h2>{escape(s["title"])}</h2><p class="eyebrow">{escape(s["type"])} · 查阅 {escape(s["accessed"])}</p>'
        + paragraphs(s.get("edition", "") + ("\n\n" if s.get("edition") else "") + s.get("use", ""))
        + f'<p><a href="{escape(s["url"])}">查看来源 ↗</a></p></section>' for s in data["sources"])


def render_glossary(data):
    return '<h1>术语与译名</h1><p>以下译法暂定。全文审校后再统一；一词多义，仍按上下文辨认。</p>' + ''.join(
        f'<section class="source-entry"><h2>{escape(t["term"])} <span class="gloss">{escape(t["translation"])}</span></h2>'
        + paragraphs(t["note"]) + f'<p class="source-links">{source_links(t["source_ids"], data)}</p></section>' for t in data["glossary"])


def reading_settings():
    return '''<dialog id="reading-settings" class="reader-dialog" aria-labelledby="reading-settings-title" aria-describedby="reading-settings-hint">
<header class="dialog-header"><div><h2 id="reading-settings-title">阅读设置</h2><p id="reading-settings-hint">设置只保存在当前浏览器</p></div><button type="button" class="dialog-close" data-close-dialog aria-label="关闭阅读设置" autofocus>×</button></header>
<div class="settings-body">
<div class="setting-row"><label for="font-size">字号</label><div class="size-stepper"><button type="button" id="decrease-font" aria-label="减小字号">A−</button><div class="size-number"><input id="font-size" type="number" inputmode="numeric" min="18" max="36" step="1" value="24" aria-label="字号"><span>px</span></div><button type="button" id="increase-font" aria-label="增大字号">A+</button></div></div>
<div class="setting-row"><label for="line-height">行距</label><div class="range-control"><input id="line-height" type="range" min="1.5" max="2.6" step="0.1" value="2.1"><output for="line-height" id="line-height-value">2.1</output></div></div>
<div class="setting-row"><span id="font-choice-label">字体</span><div class="choice-group font-choices" role="group" aria-labelledby="font-choice-label"><button type="button" data-reading-font="serif" aria-pressed="true">思源宋体</button><button type="button" data-reading-font="sans" aria-pressed="false">思源黑体</button><button type="button" data-reading-font="kai" aria-pressed="false">霞鹜文楷</button></div></div>
<div class="setting-row"><span id="script-choice-label">字形</span><div class="choice-group" role="group" aria-labelledby="script-choice-label" data-no-convert><button type="button" data-reading-script="hans" aria-pressed="true">简体</button><button type="button" data-reading-script="hant" aria-pressed="false">繁體</button></div></div>
<div class="setting-row"><span id="theme-choice-label">配色</span><div class="theme-choices" role="group" aria-labelledby="theme-choice-label"><button type="button" data-reading-theme="paper" aria-pressed="true"><span class="theme-swatch" aria-hidden="true"></span>纸张</button><button type="button" data-reading-theme="light" aria-pressed="false"><span class="theme-swatch" aria-hidden="true"></span>浅色</button><button type="button" data-reading-theme="sage" aria-pressed="false"><span class="theme-swatch" aria-hidden="true"></span>护眼</button><button type="button" data-reading-theme="dark" aria-pressed="false"><span class="theme-swatch" aria-hidden="true"></span>深色</button></div></div>
<div class="setting-row"><label for="reading-width">版心宽度</label><div class="range-control"><input id="reading-width" type="range" min="440" max="1000" step="20" value="760"><output for="reading-width" id="reading-width-value">760px</output></div></div>
<div class="setting-row"><label for="reading-margin">左右留白</label><div class="range-control"><input id="reading-margin" type="range" min="12" max="64" step="2" value="24"><output for="reading-margin" id="reading-margin-value">24px</output></div></div>
<div class="setting-row display-row"><span id="display-choice-label">显示内容</span><div class="display-choices" role="group" aria-labelledby="display-choice-label"><label><input type="checkbox" id="show-original" checked>原文对照</label><label><input type="checkbox" id="show-notes" checked>译注与出处</label></div></div>
<section class="reading-preview" aria-label="阅读效果预览"><span>预览</span><p>循河入梦，逐字寻声。</p><small>Finnegans Wake · James Joyce</small></section>
<div class="settings-footer"><button type="button" id="reset-reading">恢复默认设置</button><span>调整后即时生效</span></div>
</div></dialog>'''


def page(title, body, data, prefix="", current="", home=False):
    config = data["config"]
    menu = []
    last_book = None
    for chapter in data["chapters"]:
        if chapter["book"] != last_book:
            menu.append(f'<p class="book-label">BOOK {chapter["book"]}</p>')
            last_book = chapter["book"]
        active = ' aria-current="page"' if current == chapter["id"] else ''
        menu.append(f'<a href="{prefix}chapters/{slug(chapter)}.html"{active}><span>{escape(chapter["id"])}</span> {escape(chapter["title"].split("·")[-1])}<small>{COVERAGE[chapter["coverage"]]}</small></a>')
    utilities = (f'<a href="{prefix}glossary.html">译名</a><a href="{prefix}sources.html">资料</a>'
                 + f'<a href="{escape(config["repository"])}">GitHub ↗</a>')
    contents = ''.join(menu)
    home_styles = f'<link rel="stylesheet" href="{prefix}assets/home.css">' if home else ''
    directory = ('<dialog id="contents-dialog" class="reader-dialog contents-dialog" aria-labelledby="contents-title">'
                 + '<header class="dialog-header"><div><h2 id="contents-title">全书目录</h2><p>四卷 · 十七章</p></div>'
                 + '<button type="button" class="dialog-close" data-close-dialog aria-label="关闭全书目录" autofocus>×</button></header>'
                 + '<nav class="dialog-contents" aria-label="弹窗章节目录">' + contents + '</nav>'
                 + '<nav class="sidebar-utilities" aria-label="阅读资料">' + utilities + '</nav></dialog>')
    return ('<!doctype html><html lang="zh-Hans"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
            + f'<title>{escape(title)} · {escape(config["title"])}</title><meta name="description" content="《芬尼根的守灵夜》中文译注：原文对照、双关、出处与异译。">'
            + '<link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>'
            + '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/source-han-vf@0.1.1/source-han-serif-vf.css">'
            + '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/source-han-vf@0.1.1/source-han-sans-vf.css">'
            + '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/lxgw-wenkai-screen-webfont@1.7.0/lxgwwenkaiscreen.css">'
            + f'<link rel="stylesheet" href="{prefix}assets/style.css">' + home_styles
            + f'<script defer src="{prefix}assets/vendor/opencc-1.4.2.js"></script><script defer src="{prefix}assets/reader-model.js"></script><script defer src="{prefix}assets/reader.js"></script></head>'
            + ('<body class="home">' if home else '<body>')
            + '<a class="skip" href="#main">跳至正文</a><header class="topbar">'
            + f'<a class="brand" href="{prefix}index.html">FW<span>守灵夜译注</span></a><nav aria-label="主导航">'
            + '<span class="header-utilities">' + utilities + '</span>'
            + '<button id="contents-toggle" type="button" data-open-dialog="contents-dialog" aria-controls="contents-dialog" aria-haspopup="dialog" aria-expanded="false">目录</button>'
            + '<button id="script-toggle" type="button" data-no-convert aria-label="切换为繁体中文">繁體</button>'
            + '<button id="reading-settings-toggle" class="settings-trigger" type="button" data-open-dialog="reading-settings" aria-controls="reading-settings" aria-haspopup="dialog" aria-expanded="false"><span aria-hidden="true">Aa</span> 阅读设置</button></nav></header>'
            + reading_settings() + directory
            + '<div class="layout"><aside class="sidebar"><details open><summary>全书目录 <span>四卷 · 十七章</span></summary><nav aria-label="章节目录">'
            + contents + '</nav><nav class="sidebar-utilities" aria-label="资料链接">' + utilities + '</nav></details></aside><main id="main">' + body + '</main></div>'
            + f'<footer>James Joyce · {escape(config["title"])} · v{escape(config["version"])}<br>中文试译与原创注释 CC BY-NC-SA 4.0 · 代码 MIT</footer></body></html>')


def xhtml(title, body, stylesheet="style.css"):
    return ('<?xml version="1.0" encoding="utf-8"?>'
            + '<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="zh-Hans" xml:lang="zh-Hans"><head>'
            + f'<meta charset="utf-8"/><title>{escape(title)}</title><link rel="stylesheet" type="text/css" href="{stylesheet}"/></head><body>' + body + '</body></html>')


def build_epub(data, out):
    config = data["config"]
    items = {"sources.xhtml": xhtml("资料", render_sources(data).replace("sources.html#", "sources.xhtml#")),
             "glossary.xhtml": xhtml("译名", render_glossary(data).replace("sources.html#", "sources.xhtml#"))}
    nav = []
    for chapter in data["chapters"]:
        name = f'chapters/{slug(chapter)}.xhtml'
        body = f'<h1>{escape(chapter["title"])}</h1><p>{COVERAGE[chapter["coverage"]]} · pp. {chapter["pages"][0]}–{chapter["pages"][1]}</p>'
        body += render_segments(chapter, data, epub=True).replace("sources.html#", "sources.xhtml#")
        items[name] = xhtml(chapter["title"], body, "../style.css")
        nav.append(f'<li><a href="{name}">{escape(chapter["title"])}</a></li>')
    stats = statistics(data)
    notice = ('<h1>' + escape(config["title"]) + f'</h1><p>James Joyce · 中文译注工程</p><p>当前收录 {stats["segments"]} 段译稿，{stats["reviewed"]} 段已审校。尚未录入的正文仅列待译目录。</p>'
              + '<p>页行采用通行坐标；电子见证本、出处与存疑解读见各段注释和资料页。</p><p>中文试译及原创注释：CC BY-NC-SA 4.0。此许可不涵盖 Joyce 原著及第三方资料。来源站标示原著在加拿大属公有领域，其他地区请按当地规则使用。</p>'
              + '<p>本项目以 AI 辅助起草；没有人工审校记录的段落均保留“试译”状态。</p>')
    items["title.xhtml"] = xhtml(config["title"], notice)
    items["nav.xhtml"] = xhtml("目录", '<nav epub:type="toc" id="toc"><h1>目录</h1><ol><li><a href="title.xhtml">书名与许可</a></li>' + ''.join(nav) + '<li><a href="glossary.xhtml">译名</a></li><li><a href="sources.xhtml">资料</a></li></ol></nav>')
    manifest = '<item id="css" href="style.css" media-type="text/css"/>'
    ordered = ["title.xhtml"] + [f'chapters/{slug(c)}.xhtml' for c in data["chapters"]] + ["glossary.xhtml", "sources.xhtml"]
    for i, name in enumerate(items):
        manifest += f'<item id="item-{i}" href="{name}" media-type="application/xhtml+xml"' + (' properties="nav"' if name == "nav.xhtml" else '') + '/>'
    ids = {name: f"item-{i}" for i, name in enumerate(items)}
    spine = ''.join(f'<itemref idref="{ids[name]}"/>' for name in ordered)
    opf = ('<?xml version="1.0" encoding="UTF-8"?><package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="book-id" xml:lang="zh-Hans">'
           + '<metadata xmlns:dc="http://purl.org/dc/elements/1.1/"><dc:identifier id="book-id">' + escape(config["repository"] + "/" + config["version"])
           + '</dc:identifier><dc:title>' + escape(config["title"]) + '</dc:title><dc:creator>James Joyce</dc:creator><dc:language>zh-Hans</dc:language>'
           + '<dc:rights>Chinese translation and original notes: CC BY-NC-SA 4.0; third-party texts excluded.</dc:rights>'
           + '<meta property="dcterms:modified">' + config["date"] + 'T00:00:00Z</meta></metadata><manifest>' + manifest + '</manifest><spine>' + spine + '</spine></package>')
    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED) as book:
        book.writestr("mimetype", "application/epub+zip", compress_type=zipfile.ZIP_STORED)
        book.writestr("META-INF/container.xml", '<?xml version="1.0"?><container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container"><rootfiles><rootfile full-path="EPUB/package.opf" media-type="application/oebps-package+xml"/></rootfiles></container>')
        book.writestr("EPUB/package.opf", opf)
        book.writestr("EPUB/style.css", "body{font-family:serif;line-height:1.85;margin:6%;}p{margin:1em 0;}h1{font-size:1.5em;}h2,h3{font-size:1.1em;}.original{color:#444;border-left:2px solid #777;padding-left:1em;}aside{margin:1.5em 0;}.tag,.muted,.source-links{font-size:.85em;}a{overflow-wrap:anywhere;}")
        for name, content in items.items():
            ET.fromstring(content)
            book.writestr("EPUB/" + name, content)


def render_home(data):
    stats = statistics(data)
    first = slug(data["chapters"][0])
    last = slug(data["chapters"][-1])
    engraving = (ROOT / "site" / "river-engraving.svg").read_text(encoding="utf-8")
    hero = ('<div class="home-folio"><span>FINNEGANS WAKE</span><span>中文译注 · 持续修订</span></div>'
            + '<section class="hero"><div class="hero-copy"><p class="eyebrow"><span class="folio-rule" aria-hidden="true"></span> JAMES JOYCE</p>'
            + '<h1><span>芬尼根的</span><br><em>守灵夜</em></h1><p class="book-title-en" lang="en">Finnegans Wake</p>'
            + '<p class="lead">循河入梦，逐字寻声。</p><p class="hero-description">一部仍在生长的中文译注。让原文、异译与出处并置，让双关保留余地。</p>'
            + f'<div class="actions"><a class="button primary" href="chapters/{first}.html">从河流开始 <span aria-hidden="true">↗</span></a>'
            + '<a class="epub-link" href="downloads/finnegans-wake-zh.epub" download>下载试译 EPUB <span aria-hidden="true">↓</span></a></div></div>'
            + '<figure class="cover-art"><div class="art-caption-top"><span>RIVER / DREAM / RETURN</span><span aria-hidden="true">↺</span></div>'
            + engraving + '<figcaption><span>河流 · 梦境 · 回环</span><span lang="en">riverrun</span></figcaption></figure></section>')
    stats_markup = ''.join(f'<div><strong>{stats[key]:02d}</strong><span>{label}</span></div>' for key, label in [("chapters", "章目录"), ("segments", "段试译"), ("notes", "条译注"), ("reviewed", "段已审校")])
    hero += ('<section class="progress"><div class="section-heading"><h2>译注札记</h2><span>WORK IN PROGRESS</span></div><div class="stats">' + stats_markup
             + f'</div><p>据当前章稿统计 · {stats["complete"]} 章已核完整覆盖 · 试译仍待审校</p></section>')
    hero += ('<section class="approach"><div><p class="eyebrow">READ · LISTEN · RETURN</p><h2>读正文，也读字缝。</h2>'
             + '<p>译文尽量顺着中文呼吸。词源、典故、声音与歧义留在注内；证据不足便存疑。</p></div>'
             + f'<div class="return-note"><span class="return-word" aria-hidden="true" lang="en">riverrun</span><a href="chapters/{last}.html">到末尾听一次回声 <span aria-hidden="true">↗</span></a></div></section>')
    return hero


def build(data, out):
    errors = validate(data)
    if errors:
        raise ValueError("\n".join(errors))
    out = Path(out)
    site = out / "site"
    for path in [site / "chapters", site / "assets", site / "downloads"]:
        path.mkdir(parents=True, exist_ok=True)
    for name in ["style.css", "home.css", "reader-model.js", "reader.js"]:
        shutil.copyfile(ROOT / "site" / name, site / "assets" / name)
    shutil.copytree(ROOT / "site" / "vendor", site / "assets" / "vendor", dirs_exist_ok=True)
    stats = statistics(data)
    (site / "index.html").write_text(page("译注工程", render_home(data), data, home=True), encoding="utf-8")
    for i, chapter in enumerate(data["chapters"]):
        head = f'<p class="eyebrow">BOOK {chapter["book"]} · pp. {chapter["pages"][0]}–{chapter["pages"][1]}</p><h1>{escape(chapter["title"])}</h1>'
        head += f'<p class="status-notice">{COVERAGE[chapter["coverage"]]}。样稿尚待人工审校。</p>' if chapter["segments"] else ''
        controls = ''
        if chapter["segments"]:
            edit_url = data["config"]["repository"] + '/edit/main/manuscript/chapters/' + slug(chapter) + '.json'
            source_api = 'https://api.github.com/repos/' + data["config"]["repository"].split('github.com/')[-1] + '/contents/manuscript/chapters/' + slug(chapter) + '.json?ref=main'
            embedded = json.dumps({"chapter": chapter, "edit_url": edit_url, "source_api": source_api, "repository": data["config"]["repository"]}, ensure_ascii=False).replace('<', '\\u003c').replace('&', '\\u0026')
            controls = ('<div class="reader-controls"><label class="search-label">查找本章 <input type="search" id="reader-search" placeholder="词语或页行"></label><span class="reading-summary" id="reading-summary"></span></div>'
                        + '<details class="chapter-revisions"><summary>本章修订与提交</summary><p>在段落下方展开「修订本段」，可改译文及译注。保存后预览；确认后复制修订稿，到 GitHub 编辑页全选、粘贴并提交。</p>'
                        + '<div class="edit-actions"><button type="button" id="export-revisions">导出本章修订稿</button><button type="button" id="submit-revisions">复制修订并打开 GitHub</button>'
                        + f'<a class="button" href="{escape(edit_url)}" target="_blank" rel="noopener noreferrer">直接编辑仓库稿件 ↗</a></div><p id="revision-summary" role="status" aria-live="polite">当前显示公共译稿。</p></details>'
                        + f'<script id="chapter-data" type="application/json">{embedded}</script><p id="search-status" role="status" aria-live="polite"></p>')
        prev = data["chapters"][i - 1] if i else None
        following = data["chapters"][i + 1] if i + 1 < len(data["chapters"]) else None
        bottom = '<nav class="chapter-pager" aria-label="翻章">'
        if prev:
            bottom += f'<a href="{slug(prev)}.html">← {escape(prev["title"])}</a>'
        if following:
            bottom += f'<a href="{slug(following)}.html">{escape(following["title"])} →</a>'
        bottom += '</nav>'
        (site / "chapters" / (slug(chapter) + ".html")).write_text(page(chapter["title"], head + controls + render_segments(chapter, data) + bottom, data, "../", chapter["id"]), encoding="utf-8")
    (site / "sources.html").write_text(page("资料", render_sources(data), data), encoding="utf-8")
    (site / "glossary.html").write_text(page("译名", render_glossary(data), data), encoding="utf-8")
    (site / ".nojekyll").write_text("", encoding="utf-8")
    build_epub(data, out / "finnegans-wake-zh.epub")
    shutil.copyfile(out / "finnegans-wake-zh.epub", site / "downloads/finnegans-wake-zh.epub")
    (out / "progress.json").write_text(json.dumps(stats, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def generate_views(data, root=ROOT):
    for chapter in data["chapters"]:
        if not chapter["segments"]:
            continue
        for directory, field in [("raw-md", "original"), ("translated-md", "draft"), ("polish/dev", "translation")]:
            path = root / directory / (slug(chapter) + ".md")
            path.parent.mkdir(parents=True, exist_ok=True)
            text = f'# {chapter["title"]}\n\n<!-- 自动生成；请编辑 manuscript/chapters/{slug(chapter)}.json -->\n\n'
            for segment in chapter["segments"]:
                text += f'## {segment["locator"]} {{#{segment["id"]}}}\n\n{segment[field]}\n\n'
            path.write_text(text, encoding="utf-8")
        path = root / "annotations" / (slug(chapter) + ".json")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps({s["id"]: s["notes"] for s in chapter["segments"]}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    progress = '# 译注进度\n\n自动生成；部分试译不等于整章完成。\n\n'
    for chapter in data["chapters"]:
        progress += f'- {chapter["id"]} · pp. {chapter["pages"][0]}–{chapter["pages"][1]} · {COVERAGE[chapter["coverage"]]} · {len(chapter["segments"])} 段\n'
    (root / "publish").mkdir(parents=True, exist_ok=True)
    (root / "publish/PROGRESS.md").write_text(progress, encoding="utf-8")
    if data.get("checkpoint"):
        checkpoint = data["checkpoint"]
        current = next(c for c in data["chapters"] if c["id"] == checkpoint["chapter"])
        records = root / "progress/chapters"
        records.mkdir(parents=True, exist_ok=True)
        for chapter in data["chapters"]:
            if chapter["coverage"] != "complete" and chapter["id"] != current["id"]:
                continue
            record = {"chapter": chapter["id"], "state": "completed" if chapter["coverage"] == "complete" else "in_progress",
                      "last_segment": chapter["segments"][-1]["id"] if chapter["segments"] else None,
                      "translated_ranges": [s["locator"] for s in chapter["segments"]],
                      "reviewed_segments": [s["id"] for s in chapter["segments"] if s["status"] == "reviewed"],
                      "updated": checkpoint["updated"]}
            if chapter["id"] == current["id"]:
                record.update({"next": checkpoint["next"], "next_original": checkpoint["next_original"], "unresolved": checkpoint["notes"]})
            (records / (slug(chapter) + ".json")).write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        p, line = checkpoint["next"]
        resume = ('# 续译断点\n\n' + f'更新：{checkpoint["updated"]}\n\n当前顺序译章：**{current["id"]} · {current["title"]}**。\n\n'
                  + f'下一段从 **{p:03d}.{line:02d}** 开始，原文锚句：\n\n> {checkpoint["next_original"]}\n\n'
                  + '## 已保存\n\n' + ''.join(f'- {s["locator"]} · {s["id"]} · {STATUS[s["status"]]}\n' for s in current["segments"])
                  + '\n## 未决问题\n\n' + ''.join(f'- {note}\n' for note in checkpoint["notes"])
                  + '\n## 下次如何继续\n\n先读 AGENTS.md、本文、当前章 JSON 和来源表。核对上述锚句后，从下一段续译，不重译已保存段落。篇末回环样稿只作对读，不能据此跳过中间正文。\n\n'
                  + '每轮修改后更新 progress/checkpoint.json，运行检查、测试与构建，将稿件和断点一并提交。每章正文录入并核对覆盖后，再写 coverage_review、标 complete；工具会在 progress/chapters/ 留下章节记录。人工审校状态另记。\n\n'
                  + '未完成全书前保留长期目标。版本以 git log 和 GitHub 提交为准，不凭聊天摘要判断进度。\n')
        (root / "progress/RESUME.md").write_text(resume, encoding="utf-8")


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.links, self.duplicates = set(), [], []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            if attrs["id"] in self.ids:
                self.duplicates.append(attrs["id"])
            self.ids.add(attrs["id"])
        for key in ["href", "src"]:
            if key in attrs:
                self.links.append(attrs[key])


def check_artifacts(out):
    out = Path(out)
    errors = []

    def inspect(files):
        parsed = {}
        for name, content in files.items():
            if name.endswith((".html", ".xhtml")):
                parser = Links()
                parser.feed(content.decode("utf-8"))
                parsed[name] = parser
                errors.extend(f"duplicate artifact ID: {name}#{i}" for i in parser.duplicates)
        for name, parser in parsed.items():
            for link in parser.links:
                parts = urlsplit(link)
                if parts.scheme or parts.netloc:
                    continue
                import posixpath
                target = posixpath.normpath(posixpath.join(posixpath.dirname(name), unquote(parts.path))) if parts.path else name
                if target not in files:
                    errors.append(f"missing artifact target: {name} -> {link}")
                elif parts.fragment and (target not in parsed or unquote(parts.fragment) not in parsed[target].ids):
                    errors.append(f"missing artifact anchor: {name} -> {link}")

    site = out / "site"
    if not (site / "index.html").exists():
        errors.append("missing site index")
    inspect({str(p.relative_to(site)): p.read_bytes() for p in site.rglob("*") if p.is_file()})
    epub = out / "finnegans-wake-zh.epub"
    if not epub.exists():
        errors.append("missing EPUB")
        return errors
    with zipfile.ZipFile(epub) as book:
        files = {name: book.read(name) for name in book.namelist()}
        for name, content in files.items():
            if name.endswith((".xhtml", ".xml", ".opf")):
                ET.fromstring(content)
        inspect(files)
        opf = ET.fromstring(files["EPUB/package.opf"])
        ns = {"o": "http://www.idpf.org/2007/opf"}
        items = opf.findall("o:manifest/o:item", ns)
        item_ids = {item.attrib["id"] for item in items}
        for item in items:
            if "EPUB/" + item.attrib["href"] not in files:
                errors.append(f"missing EPUB manifest file: {item.attrib['href']}")
        for itemref in opf.findall("o:spine/o:itemref", ns):
            if itemref.attrib["idref"] not in item_ids:
                errors.append(f"unknown EPUB spine item: {itemref.attrib['idref']}")
    return errors


def main():
    parser = argparse.ArgumentParser(description="《芬尼根的守灵夜》译注检查与构建")
    parser.add_argument("command", choices=["check", "generate", "build", "check-artifacts"])
    parser.add_argument("--out", type=Path, default=ROOT / "dist")
    args = parser.parse_args()
    if args.command == "check-artifacts":
        errors = check_artifacts(args.out)
    else:
        data = load_project()
        errors = validate(data)
        if not errors and args.command == "generate":
            generate_views(data)
        elif not errors and args.command == "build":
            generate_views(data)
            build(data, args.out)
            errors = check_artifacts(args.out)
        if not errors:
            print(json.dumps(statistics(data), ensure_ascii=False))
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("检查通过" if args.command in ("check", "check-artifacts") else "生成完成")
    return 0


if __name__ == "__main__":
    sys.exit(main())
