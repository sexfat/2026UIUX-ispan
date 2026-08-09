# 修復與調整紀錄

---

## 2026-06-29

### 1. 深色投影片的上下頁按鈕配色修正
**問題：** Unit 01、Unit 02 簡報在黑底（`.dark`）投影片時，右下角的上一頁／下一頁按鈕仍是深色，幾乎看不見。
**原因：** `#ctrls button` 採固定深色樣式（`rgba(29,29,31,.06)` + 深色文字），未隨投影片深淺背景切換。
**修正：** 翻頁時偵測目前投影片是否為 `.dark`，是則為控制列加上 `on-dark` class，按鈕改為白色半透明（hover 更亮）；切回淺色頁自動恢復。初始載入也會判斷第一頁。
**影響範圍：**
- `Unit_01/slides_unit01.html` — 新增 `#ctrls.on-dark` 樣式與 go()／初始化的 class 切換
- `Unit_02/slides_unit02.html` — 同上

### 2. 文章參考資料區塊暫時隱藏
**問題：** `article.html` 最下方「參考資料」區塊需暫時不顯示。
**原因：** 依需求暫時隱藏，但保留內容供日後恢復。
**修正：** 將 `.refs` 區塊以 HTML 註解包起（`<!-- ... -->`），需要時移除註解即可恢復。
**影響範圍：**
- `Unit_02/article.html` — 註解 `.refs` 區塊

### 3. 首頁連結改為另開新頁
**問題：** `index.html` 的連結預設在原分頁開啟。
**原因：** 需讓使用者點擊單元素材時不離開課程總覽頁。
**修正：** 為全部 6 個連結（Unit 01 ×2、Unit 02 ×3、頁尾課程大綱）加上 `target="_blank" rel="noopener"`。
**影響範圍：**
- `index.html` — 各 `<a>` 連結加上 target／rel

---

## 2026-08-02

### 1. Unit 05 講義的課堂練習時間未跟著改
**問題：** Unit 05 課堂練習時間從 90 分鐘調整為 80 分鐘時，簡報、練習頁、README 都改了，`article.html` 第 13 節卻仍寫「課堂練習：電商後台卡片分類法（90 分鐘）」，四階段時間也還是舊的 30／20／25。
**原因：** 同一個數字散在四個檔案，靠人工記憶同步，漏掉最不常回頭看的講義。
**修正：** 講義改為 80 分鐘與 25／18／22，並補上「四階段結束後另有 15 分鐘成果分享」。同時把 `exercises.html` 開頭 lead 的「用 90 分鐘跑完」一併改掉。這個問題是新寫的 `validate.py` 對帳報表列出時間數字後才發現的。
**影響範圍：**
- `Unit_05/article.html` — 第 13 節課堂練習時間與四階段時間
- `Unit_05/exercises.html` — hero lead 的時間敘述

### 2. 驗收腳本兩處漏檢
**問題：** `validate.py` 初版在其他單元上跑出假警報，且漏掉最該對帳的數字。
**原因：** 一是只認 `<section class="slide">` 與 `<p class="sec-num">數字</p>`，但 Unit_01–03 用的是 `<div class="slide">` 與 `SECTION 01` 前綴；二是時間數字的正則只抓「分／分鐘」，而簡報 Agenda 寫的是 `50 min`，導致課程總長沒進對帳報表。
**修正：** 標記比對放寬為 `(?:section|div)`、`sec-num` 允許非數字前綴；時間正則加入 `min`／`mins`。另外對於完全不使用 `.section` 結構的舊單元（Unit_02），改為輸出提示並跳過節號檢查，不再報成錯誤。
**影響範圍：**
- `.claude/skills/unit-materials/validate.py` — 標記相容性與時間數字擷取

---

## 2026-08-07

### 1. Unit 08 簡報封面標示的張數與實際會播的張數對不起來
**狀態：** 已修復
**問題：** `Unit_08/slides.html` 封面 `cover-meta` 寫「29 張投影片」，但第一頁右上角的頁碼顯示的是「01 / 22」。學生看到的兩個數字互相矛盾。
**原因：** 檔案裡有 7 張投影片被標記為備用補充頁（`class="slide ... drop"`）。`.slide.drop { display: none }` 讓它們不顯示，翻頁 JS 也用 `.slide:not(.drop)` 收集頁面，所以自動填的頁碼分母是 29 − 7 ＝ 22。但 `cover-meta` 是寫死的字串，不會跟著 `drop` 的增減走。README 也寫「29 張，其中 7 張為備用補充頁」，跟封面同一套算法，但跟畫面上的頁碼不同。
**佐證：**
```
$ grep -c '<section class="slide' Unit_08/slides.html        → 29
$ grep -c 'class="slide[^"]*drop' Unit_08/slides.html         → 7
$ grep -n '\.drop' Unit_08/slides.html
605:.slide.drop { display: none; }
1341:      const slides = Array.from(document.querySelectorAll('.slide:not(.drop)'));
```
排除掉的可能：不是 `drop` 沒有掛樣式或 JS（早先看的版本確實沒有，現在 CSS 與 JS 兩處都補上了），純粹是封面那個手寫數字沒跟著改。
**修正：** 採方向 ①，對外的數字一律用會播的張數。`cover-meta` 改成「22 張投影片 · 另有 7 張備用補充頁與 Figma 實作」，README 改成「22 張，另有 7 張標了 `drop` 的備用補充頁，預設不播」。沒有改用 JS 動態寫入，因為 `cover-meta` 裡還有其他寫死的文字，不值得為一個數字多掛一段初始化邏輯。
另外補上 `validate.py` 的漏檢：`check_slides()` 原本用 `<(?:section|div) class="slide[\s"]` 數總數，改成抓完整 class 字串後扣掉含 `drop` 的，比對封面標示時用會播的張數，並在報表註明備用頁有幾張。Unit_03／05／06／07／08 重跑全綠。
**影響範圍：**
- `Unit_08/slides.html` — `cover-meta` 的「29 張投影片」（查證位置：CSS 605 行、JS 1341 行）
- `Unit_08/README.md` — 第 6 行「課堂簡報（29 張，其中 7 張為備用補充頁）」
- `.claude/skills/unit-materials/validate.py` — `check_slides()` 張數比對排除 `.drop`
