# 首页艺术设计实施计划

> **For agentic workers:** 使用 superpowers:executing-plans 按项实施。

**Goal:** 保留首页气质，细修标题、留白、原创线刻与进度栏。

**Architecture:** 首页使用独立 body 类与样式；构建时嵌入静态 SVG，统计仍取章稿。章节页不加载首页样式。

**Tech Stack:** Python 标准库、HTML、CSS、SVG。

**Spec:** `docs/superpowers/specs/2026-10-31-home-art-direction.md`

## Global Constraints

- 不改章稿、译注、出处、审校状态或断点。
- 沿用开源字体、四主题及简繁切换；不增框架或持续动画。

## Review Focus

- 375px、768px、1440px 均无横向溢出。
- 深色与护眼模式保持字色对比，线刻不盖住文字。
- 页面无需脚本也能显示正文；图形不增加屏幕阅读负担。
- 章节页不引入首页样式，统计仍取实际稿件。
- 发布时保留远端并行改动，只上传本次文件。

## Task

- [x] 修改首页模板，保留阅读与下载入口；新增 `site/home.css` 与 `site/river-engraving.svg`。
- [x] 检查图形语义、统计、链接及主题；核手机与桌面版式。
- [x] 执行仓库检查、测试、构建与产物检查，独立复核差异。
- [ ] 基于最新远端合入，核 Pages 部署和线上实景。
