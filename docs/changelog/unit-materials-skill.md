# [LOG] unit-materials skill 與教材驗收腳本

對應規格：[docs/spec/unit-materials-skill.md](../spec/unit-materials-skill.md)

---

## 2026-08-02 — 建立 skill 與 validate.py，並補上語調規範

**修改檔案：**
- `.claude/skills/unit-materials/SKILL.md` — skill 主體（新增）
- `.claude/skills/unit-materials/references/design-system.md` — 設計系統契約（新增）
- `.claude/skills/unit-materials/references/content-traps.md` — 內容正確性檢查（新增）
- `.claude/skills/unit-materials/references/figma-board.md` — Figma 板建置指引（新增）
- `.claude/skills/unit-materials/references/tone.md` — 語調規範（新增）
- `.claude/skills/unit-materials/validate.py` — 驗收腳本（新增）

**實作說明：**

*結構*
依 `writing-great-skills` 的規範撰寫：model-invoked、SKILL.md 保持精簡、細節透過 context pointer 下推到 reference。核心是五個 leading word——講課、溯源、對標、對帳、驗收——每個都是「每次動筆都要盯」而非「寫完再檢查」的事，因此都放在 SKILL.md 主體而非 reference。

*語調（後續追加）*
用戶另外要求把「老師在課堂上講解」的語氣固化進來。作法是把它當成第五根柱子而非附註，排在最前面，因為它管的是每一句怎麼寫。`tone.md` 收錄 AI 腔句型對照表（「這帶出一個重要的實務含意」「綜上所述」「透過本單元的學習，學生將能夠…」）與六組實際改寫範例——全部取自 Unit 05 教材裡真實出現過的句子。另外拆出三份檔案的語調差異：簡報最口語、句子最短；講義是講稿的展開版；練習頁用祈使句下指令並說明為什麼。

*validate.py*
把「對帳」從提醒變成可執行的檢查。設計原則是**只驗證機器能確定的事**：結構、id、連結、錨點、class、編號連續性、跨檔的「第 N 節」引用；時間數字只列成報表，不判對錯——因為「50 分是 Part 1 還是課堂練習」需要語意判斷，交給正則會產生假警報。

寫完後對 Unit_01–06 逐一試跑，修掉兩處相容性問題（見下方備註），並當場抓到兩個真實錯誤。

**已知問題 / 備註：**
- **相容性修正**：初版只認 `<section class="slide">` 與 `<p class="sec-num">數字</p>`，但 Unit_01–03 用 `<div class="slide">` 與 `SECTION 01` 前綴，會報假警報。已放寬為 `(?:section|div)` 與允許非數字前綴。Unit_02 的講義完全不使用 `.section` 結構，改為輸出提示並跳過節號檢查。
- **時間正則漏洞**：初版只抓「分／分鐘」，但簡報 Agenda 寫的是 `50 min`——課程總長正好住在那裡，所以最該對帳的數字反而沒進報表。已加入 `min`／`mins`。
- **腳本抓到的真實問題**：① Unit_05 講義第 13 節仍寫「課堂練習 90 分鐘」（已修，見 `future/maintain.md`）；② `Unit_09/slides.html` 封面寫「21 張投影片」但實際 22 張——**尚未修正**，屬既有內容，等用戶確認。
- skill 需要重啟 session 才會被註冊，同一個 session 內只能手動照檔案流程走。
