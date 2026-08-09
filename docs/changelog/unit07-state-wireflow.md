# [LOG] Unit 07 完整教材建置（狀態設計與 Wireflow 合成）

對應規格：[docs/spec/unit07-state-wireflow.md](../spec/unit07-state-wireflow.md)

---

## 2026-08-07 — 依新主題重製 Unit 07 全套教材，並建立 Figma 練習範本與作業題目卡

**修改檔案：**
- `Unit_07/resources/guide.md` — NN/g 九篇來源整理（新增）
- `Unit_07/slides.html` — 25 張投影片（整份取代舊的 5 張佔位內容）
- `Unit_07/article.html` — 13 節長文教材（新增）
- `Unit_07/exercises.html` — 課堂練習與回家作業（新增）
- `Unit_07/README.md` — 單元架構、時間分配、練習與作業（重寫）
- `index.html` — Unit 07 卡片描述與三個入口

**實作說明：**

先補來源。`Unit_07/resources/` 原本是空的，等於這個單元沒有溯源依據，所以任何教材內容都不能寫。整理 NN/g 九篇成 `guide.md`，每條保留英文原句，最後一節是「來源 → 課程哪一段用到」的對照表。Wireflow 定義與保真度那部分不重抄，直接指向 `Unit_06/resources/guide.md` §1。

版型對標最新單元。`slides.html` 的 head 與 CSS 用 Python 從 `Unit_08/slides.html` 以 `</head>` 切開整段沿用；`article.html` 抄 `Unit_03/article.html`；`exercises.html` 抄 `Unit_06/exercises.html`（它已有 `.band`、`.exercise.home`、`.check`、`.bad`／`.good`）。新增的兩個 class 都補了深色規則：`.wf .ph`（線框佔位塊，含 `b`／`em` 的 `.slide.dark` 覆寫，深色藍用 `#58a6ff`）與 `.matrix.c5`。全程沒有用 `.dia`／`.flow-dia` 排任何文字流程圖。

時間對帳三處。Part 1 45 ＋ 休息 10 ＋ Part 2 25 ＋ Part 3 85 ＋ Part 4 15 ＝ 180，對上 `index.html` 的 09:00–12:00；練習四階段 15＋25＋20＋25 ＝ 85，對上簡報 Part 3；階段內部 25 分拆 10／10／5、20 分拆 12／8、25 分拆 10／10／5。簡報張數隨內容增刪三次（26 → 24 → 25），每次都同步 `cover-meta` 與 README。

Figma 檔由這邊建，不是 Codex 建。`codex exec` 在 headless 模式下呼叫 `use_figma` 會直接回 "user cancelled MCP tool call"（需要互動式核准），所以練習範本與題目卡都是載入 figma-use skill 後自己建的。中文字型用 `Noto Sans TC`（Inter 沒有中文字）。

**內容審查（Codex 對照 `resources/guide.md`）—— 五處觀念錯誤已修：**
- 簡報寫「接下來三十分鐘」，但 Agenda 的 Part 2 是 25 分 → 改成「接下來這 25 分鐘」。
- Wireflow 寫成「**就是**『wireframe 的版面設計 + 簡化過的流程圖式互動表示法』」，把 NN/g 的描述講成絕對定義 → 改成「NN/g 對 Wireflow 的定義是：……」。
- 表單第 10 條寫成「不要讓同一個錯誤發生第三次」，等於自己造了一條「第三次就是違規」的規則 → 改成「同一個錯誤重複出現要給額外協助……三次不是規定，是一個提醒你『這裡設計有問題』的訊號」。
- 簡報的角色表漏了引導者（Facilitator）→ 補一列。
- 被動通知窄化成「角落一個小紅點就夠」→ 改成「常見做法是一個 badge（角落的小紅點或數字）」。

**教學設計調整（Codex 提出、用戶同意）：**
- 課堂標註要求原本每張畫面 3 條，20 分鐘內做不完 → 課堂上每張先寫 1 條關鍵標註，回家補到 3 條。
- 作業「3–5 個 Wireframe」與「三種狀態各一張」在算法上會打架 → 明確寫成 3–5 指的是**核心畫面**，狀態版本不另計數。
- 配分表原本只有「不及格的樣子」→ 補上「通過的樣子」一欄，讓評分尺度兩邊都有錨點。
- 用戶要求整體再精簡，主軸收回到空狀態／錯誤狀態／載入狀態三件事，Part 2 的檢核內容壓縮，較細的（critique 與 review 的差別、五個常見失敗、兩種帶法）只留在講義不進簡報。

**Figma 檔（`X0nEWewUts2YSRElqN6dE3`，team Ateam）：**
- 分頁「Unit 07 練習範本」：① 狀態盤點表 ② 三種狀態範本 ③ 標註格式範本 ④ 修正紀錄表，四組各對應課堂練習一個階段，學生複製區塊到自己的檔案填寫。
- 分頁「作業題目」（`?node-id=6-2`）：題目 1 會員註冊與登入（Unit 06 練過的基準題）、題目 2 結帳付款出錯（練錯誤狀態的四種層級，加一段超過 10 秒的付款等待）、題目 3 中途離開與返回（練五種「往回」的差別：上一步／手機返回鍵／切出去再切回來／按取消／送出後想改）。每張題目卡含情境、Persona、必須畫出的狀態、容易踩的坑、交件清單與五個空白畫框。
- 三個題目已嵌入簡報（新增一張「今天要改哪一條流程」）、講義第 12 節開頭、`exercises.html` 的前置說明與資源列，以及 README。

**已知問題 / 備註：**
- `Unit_07/resources/` 目前只有 `guide.md`，沒有任何圖檔。原本打算從 Pinterest 取錯誤狀態的好壞對照範例，但該站為 JS 渲染且有登入牆，`WebFetch` 只回得到截斷的殼，取不到圖片網址；加上第三方圖片授權問題，最後未納入。若之後要補，建議自己在 Figma 做好／壞對照再匯出 PNG 放進 `resources/`。
- 舊的 5 張佔位簡報（介面視覺基礎）是整份取代，沒有另存備份——該主題現由 Unit 08 涵蓋。
