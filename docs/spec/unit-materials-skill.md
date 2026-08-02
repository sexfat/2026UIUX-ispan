# [SPEC] unit-materials skill 與教材驗收腳本

- **日期**：2026-08-02
- **負責人**：bryant_huang
- **狀態**：done
- **變更紀錄**：[docs/changelog/unit-materials-skill.md](../changelog/unit-materials-skill.md)

---

## 背景

Unit 05 教材製作過程中，重複踩到同一類問題：

- **時間對不起來**：課堂練習時間散在簡報、練習頁、README，改一處忘三處，最後三份文件加總超過課程總長。
- **交叉引用會歪**：講義插入新小節後全檔重編號，`#sN` 錨點、side-nav、TOC 與其他檔案的「講義第 N 節」全部失準。
- **語調容易寫成 AI 腔**：「首先／其次／此外／最後」的制式結構、抽象形容詞堆疊，跟「老師在課堂上講解」的要求相反。
- **內容正確性靠 Codex 事後抓**：三模型誤把 Sitemap 算進去、把「常用於」寫成「就是」這類錯誤，沒有事前的檢查清單。

這些不該靠每次記得，應該變成流程與可執行的驗證。

## 功能說明

專案範圍（`2026UIUX-Class/.claude/skills/`）的 model-invoked skill，在用戶說「做 Unit XX 的簡報」「寫講義」「加課堂練習」「重製某單元」時觸發。

SKILL.md 以五個 leading word 組織，每項附可檢查的完成條件：

| Leading word | 管什麼 | 完成條件 |
| :--- | :--- | :--- |
| **講課** | 語調 | 隨機挑三段唸出來，像人在講話不像念稿 |
| **溯源** | 內容依據 | 每個小節都答得出來自 resources 的哪一段 |
| **對標** | 設計系統 | 色票與參照單元一致，新 class 都有 `.slide.dark` 對應 |
| **對帳** | 重複的數字 | 時間、張數節數、交叉引用都在所有檔案確認過 |
| **驗收** | 可執行檢查 | `validate.py` 全綠且時間報表加總正確 |

細節下推到四份 reference，依任務性質載入。

`validate.py` 把「對帳」從提醒變成可執行：檢查 HTML 結構、重複 id、內部連結與跨檔錨點、未定義 CSS class、簡報張數與封面標示是否相符、講義節號連續性、side-nav／TOC 錨點對齊、「第 N 節」交叉引用；時間數字則列成報表供人工判讀（語意判斷不交給正則）。

## 實作範圍

- `SKILL.md`：五個核心章節 + 練習設計、Figma 板、收尾流程。
- `references/design-system.md`：色票、三份檔案的骨架契約、必備 class 與 JS 行為、`.ilink` 樣式、三份檔案的連結網。
- `references/content-traps.md`：UX 觀念的通則錯法、六條已知具體錯誤對照表、Codex 審查提示詞骨架。
- `references/figma-board.md`：FigJam section 相對座標、TableNode 無 resize、Codex headless 寫不了 Figma、中文字型、卡片顏色統一原則。
- `references/tone.md`：AI 腔句型對照表、六組實際改寫範例、三份檔案的語調差異。
- `validate.py`：可執行驗收，相容 Unit_01–06 的標記變體。

## 不在範圍內

- **自動判斷時間是否正確**：腳本只列出所有時間數字，加總與語意由人判斷。把「50 分是 Part 1 還是練習」交給正則會產生假警報。
- **語調的自動檢查**：`tone.md` 是給人與 Codex 讀的準則，沒有寫成 lint 規則。
- **舊單元的回頭修正**：腳本對 Unit_01–03 的舊寫法採相容而非強制，不要求既有單元改成新結構。
- **全域安裝**：skill 放在專案 `.claude/skills/`，只在這個課程 repo 生效。

## 驗收條件

- [x] SKILL.md 五個核心章節各有可檢查的完成條件
- [x] 四份 reference 各自可獨立閱讀，SKILL.md 有對應的 context pointer
- [x] `validate.py` 對 Unit_01、Unit_02、Unit_03、Unit_04、Unit_05、Unit_06 皆可執行且不產生假警報
- [x] 腳本實際抓到真實問題：Unit_05 講義的 90 分鐘漏改、Unit_09 封面張數與實際不符
- [x] 時間報表涵蓋中文「分／分鐘」與英文 `min`（課程總長寫在 Agenda 的 `50 min`）
- [x] `tone.md` 的改寫範例取自實際教材，非虛構
