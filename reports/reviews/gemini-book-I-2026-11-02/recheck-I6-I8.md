# I.6–I.8 四项定点复核

## 输入与范围

- role: `ai_review`。
- executor: Codex 子代理 `/root/audit_i6_i8_latest`。AI 复核，不填人工审校者。
- 本次仅复核前报告 N-01 至 N-04，以及四处相邻句；没有重开全章或另做全章审校。
- 前报告：`/private/tmp/fw-book-I-intake-20261102/review-I6-I8.md`；SHA256：`93f3194eb3fddd60b76fadc9e3df58ca043435530521285bdffd4498db2abbf7`。其原文、覆盖及未改部分结论沿用；其外部出处未核限度仍有效。
- 实际整合记录：`/private/tmp/fw-full-source-20261101/reports/revisions/book-I-codex-integration-20261102.json`；SHA256：`23d73432fd2459bc6dcf5d48e23d27f3a36d017a7a2d6ac07415f99877d365b9`。已读 N-01 至 N-04 四项 before/after、`limits` 与 `decision`。
- revision_round: 本次针对前报告四项意见作一次修订后复核，不另推定此前修订轮次。

实际新稿文件 SHA256：

- `/private/tmp/fw-full-source-20261101/manuscript/chapters/I-6.json`：`07ba55b09e0a92a9a51f50ea31b32725afee2e9ef37e400f8489385272592c46`。
- `/private/tmp/fw-full-source-20261101/manuscript/chapters/I-7.json`：`42ec08b826ff60e12a0febd11698569a02134c256f7c8991c2175d684ecd0667`。
- `/private/tmp/fw-full-source-20261101/manuscript/chapters/I-8.json`：`36f23789bb4ccd25a3aafbc95c842502e2ad7ed793fa6e175f3c888769cce900`。

只作机械差异核对，确认三章段落 ID 与次序、全部 `original`、`draft`、`locator`、`range`、`notes` 均与冻结输入相同。`translation` 仅四个目标段发生改动；每个目标段恰为交接所列替换，没有额外正文变化。新增 `source_text` 不作为本轮重译或换本依据。

三章 `coverage_review` 均已明说“这是AI覆盖与语义复核，非人工终审；未逐项外核典故、词源或逐页复算行号”。本轮未逐项重验外部出处、印本行号或图像，不能将这份局部复核写成人工终审或全出处通过。

## 四项处置

### N-01：已解决

- 位置：`fw-i6-126-01`，126.01–129.26。
- 原句：`forbids us our trespassers as we forgate him;`
- 新译：“不许我们接纳冒犯我们的人，正如我们把他遗忘在门外”。
- 复核：保留禁阻、我们与冒犯者三层关系；不再将人改成“他的领地”。“接纳”补足禁阻关系，属可接受译法选择。本轮不据此新增阻断项。
- 上下文：前接圣火引火人，后接凤凰与灰烬，分号累积关系未变；未借修句补叙事因果。
- disposition: `resolved`。
- blocks_integration: `false`。

### N-02：已解决

- 位置：`fw-i6-163-29`，163.29–168.14；联读注 `i6-brother-foot-him-out`。
- 原句：`though it broke my heart to pray it, still I'd fear I'd hate to say!`
- 新译：“纵使祈求这般结局会教我心碎欲裂，我只怕依然不愿亲口说出那句话！”
- 复核：“不愿”恢复难以说出口的迟疑，消除“恨不能”反成急欲说的错误；与该注指出的手足犹疑相合。
- 上下文：亲兄弟、同床同蚤等假设仍在，接第十二问 `Sacer esto? / Semus sumus!` 的次序未动。
- disposition: `resolved`。
- blocks_integration: `false`。

### N-03：已解决

- 位置：`fw-i7-187-24`，187.24–193.30。
- 原句：`accomplished women, indeed fully educanded, far from being old and rich behind their dream of arrivisme, if they have only their honour left, and not deterred by bad weather when consumed by amorous passion`
- 新译：“她们才艺双全，确曾受过完备教育，心怀发迹幻梦，却谈不上年老富有；即使只剩名节，一旦欲火焚身便不畏恶劣天气”。
- 复核：否定现已同时管到“年老富有”，删掉无依据的“自有丰厚家底”和“色衰”；保留发迹幻梦、名节与不畏天气之间的关系。
- 上下文：前接众女子及流沙比喻，后接争相扑抢、孤男寡女与婚姻纽带，动作对象未变。
- disposition: `resolved`。
- blocks_integration: `false`。

### N-04：已解决

- 位置：`fw-i8-196-01`，196.01–201.20。
- 原句：`and if he didn't peg the platteau on her tawe, believe you me, she was safe enough.`
- 新译：“只要他没把托盘砸在她脑门上，信我的话，她就还算安全。”
- 复核：未砸托盘为条件，“还算安全”为结果，消除旧句“要不是他没……”的逆向双重否定。
- 上下文：前接摔开吃食，后接安娜请求哼唱，条件句没有反转或替换前后动作。
- disposition: `resolved`。
- blocks_integration: `false`。

## 结论

- 当前版本：`ready`，仅指本次四项及相邻句复核；结合前报告对未改部分的全文阅读使用，不将本次写成再次全章审校。
- N-01、N-02、N-03、N-04 均已解决。本次已核范围未见须改问题，无新增阻断项。
- 前报告的正文覆盖判断可沿用于未改部分；未核外部注释出处、印本逐行与版面等限度保留。
- 只写本报告；未改输入、公共章稿、来源、断点或人工审校署名，未执行推送。

## 四段 original_sha256

- `fw-i6-126-01`：`f3fab540d81d164b781d1453fdfd1621c144b21f033c3b59a1d9411f90f6f3fe`。
- `fw-i6-163-29`：`38c6c0a277cc00bfe98036aa51e3a86f9b96750bc66bae98a11e517bd57f4699`。
- `fw-i7-187-24`：`f14e17539917bb290e43ff46fc191bbd581a11e797b925ad70fb5c5363146e11`。
- `fw-i8-196-01`：`70056db7b12cc54ee10dc7693cf065663159cdf80cd487794e114ce387b1518e`。
