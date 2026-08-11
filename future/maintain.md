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

---

## 2026-08-11

### 1. RWD vs AWD 的示範網站實測不成立
**狀態：** 已修復
**問題：** Unit 09 簡報第 8 張要學生「用手機與桌機各開一次 PChome（RWD）與 momo（AWD），觀察載入行為的差異」。實際照做看不到差異，示範會失敗。
**原因：** 這段是從 master 分支的 Unit_12 逐字沿用下來的舊教材。用桌機與手機 User-Agent 實測，`www.momoshop.com.tw` 對兩種 UA 回的 HTML **完全相同**（byte-identical），不會依裝置轉址；`m.momoshop.com.tw` 雖然存在（HTTP 200），但要手動輸入才進得去。PChome 則因為擋爬蟲，兩種 UA 都只回空殼頁（142 bytes 對 1848 bytes），量不到有效結果。
**佐證：**
```
# 手機 UA 是否換網址（curl -sL -w %{url_effective}）
www.momoshop.com.tw   → https://www.momoshop.com.tw/main/   （未轉址）
www.etmall.com.tw     → https://m.etmall.com.tw/            （轉址）
www.ruten.com.tw      → https://www.ruten.com.tw/m/         （轉址）
591.com.tw            → https://m.591.com.tw/               （轉址）

# 同網址、兩種 UA 的 HTML 差異
www.momoshop.com.tw/main/  桌機 9832 / 手機 9832 bytes  → 完全相同
www.thsrc.com.tw           桌機 236527 / 手機 236527    → 完全相同
591.com.tw                 桌機 330032 / 手機 6079      → 兩套不同的站
```
排除掉的可能：不是 momo 沒有行動版（`m.momoshop.com.tw` 確實存在），是 www 入口不做 UA 轉址，因此「開同一個網址觀察差異」這個操作步驟本身不成立。另外 curl 只測得到伺服器端對 UA 的反應，client-side JS 轉址測不到，所以「沒換網址」不能反推一定是 RWD，但「有換網址」可以確定是 AWD。
**修正：** 示範對象換成實測有轉址行為的 **591**（AWD）與 HTML byte-identical 的 **台灣高鐵**（RWD）。591 特別適合教學：網址列會當場從 `591.com.tw` 變成 `m.591.com.tw`，分頁標題還自報「591 觸屏版」，桌機 330 KB 對行動版 6 KB 的落差也很直觀。README 補上實測對照表與另外兩個 AWD 案例（東森購物、露天市集），並記錄為什麼把 momo 換掉。兩處都註明是 2026/08/10 實測，提醒上課前重新確認。
**影響範圍：**
- `Unit_09/slides.html` — 第 8 張的比較表欄位與現場驗證說明
- `Unit_09/README.md` — 新增「課堂現場驗證的實例」對照表與換掉 momo 的原因

### 2. 各單元簡報播放中無法回到課程總覽
**狀態：** 已修復
**問題：** 14 份簡報（Unit 01–12 主簡報 + Unit 08、09 兩份補充簡報）的封面都沒有回 `index.html` 的入口，播放時只能改網址或按瀏覽器上一頁。
**原因：** 各單元簡報是不同時期做的，封面只放單元徽章與頁碼，從來沒有規劃回首頁的動線。講義與練習頁的 `foot-nav` 有「回到課程總覽」，簡報沒有。
**佐證：**
```
$ grep -l "index.html" Unit_*/slides*.html
Unit_09/slides.html      # 命中的是 sexfat.github.io/rwd/index.html 等外部示範網址
Unit_12/slides.html      # 同上
→ 實際上 14 份簡報沒有任何一份連得回 ../index.html
```
另外查證過三件事：`.slide-head` 沒有任何直接子選擇器或 `nth-child` 依賴（加第三個子元素不會破版）、專案內無 `to-index` 命名衝突、14 份封面全部是淺色頁（`currentColor` 取色安全）。
**修正：** 每份簡報的第一張封面，把單元徽章與新的「↩ 課程總覽」連結包進一個 `display:inline-flex` 容器，`slide-head` 維持「兩個子元素 + space-between」的原本佈局，頁碼位置不受影響。Unit_11 的 class 命名與其他單元不同（`head`／`unit`／`num`），個別對應處理。
第一版把樣式寫成 inline style，被 `validate.py` 抓出「使用但未定義的 class `to-index`」，改為在各檔 `<style>` 內新增 `.to-index` 規則（含 hover 由 55% 透明度轉全亮）。
**影響範圍：**
- `Unit_01/slides_unit01.html`、`Unit_02/slides_unit02.html`、`Unit_03`–`Unit_07`、`Unit_10`、`Unit_12` 的 `slides.html` — 封面連結與 `.to-index` 樣式
- `Unit_08/slides.html`、`Unit_08/gestalt-lawsofux.html`、`Unit_09/slides.html`、`Unit_09/usability-heuristics.html`、`Unit_11/slides.html` — 同上

### 3. Unit 11 教材樣式與其他單元不一致
**狀態：** 已修復
**問題：** Unit 11 的簡報與講義用的是另一套設計系統，色票、結構 class 與元件命名都跟 Unit 03–10 不同，從首頁點進去風格明顯斷裂。講義另有結構缺漏，`validate.py` 報三個錯。
**原因：** Unit 11 教材由另一個工作階段獨立建置，沒有沿用 `unit-materials` skill 的對標規則。簡報用 `--paper`／`--ink`／`--ios`／`--android` 等自訂 token 與 `head`／`unit`／`num`／`body`／`foot` 的 class 命名；講義缺 `side-nav`、`refs`，且 `sec-num` 寫成「01 · Context」，數字在後面的文字之前，不符合驗證腳本的格式。
**佐證：**
```
$ python3 .claude/skills/unit-materials/validate.py Unit_11
✗ article.html：sec-num 有 0 個，section id 有 10 個
✗ article.html：找不到 side-nav
✗ article.html：找不到 toc

# validate.py 第 142 行的正則
nums = re.findall(r'<p class="sec-num">[^<\d]*(\d+)\s*</p>', src)
→ 容許數字「前面」有標籤（Unit_03 的「SECTION 01」），不容許後面還有字
```
**修正：** 簡報換皮——色票整組換成標準色（與 Unit_10 逐項比對一致），平台區分改用 iOS→`--accent`、Android→`--accent2`；結構 class 對齊 `slide-head`／`unit-pill`／`slide-num`／`slide-body`／`slide-foot`，頁尾第二個標語欄改成圓點導航，深色頁的圓點與翻頁按鈕自動反白。固定 1920×1080 畫布、`localStorage` 記憶頁碼、分頁標題跟著投影片變這三項是本單元特有且堪用，予以保留；手機模型、Safe Area、觸控目標等平台示意圖只換色票，比例未動。
講義換成 Unit_08 的標準 CSS，補上 `side-nav`、`refs`、`sec-title`、表格的 `tbl-wrap` 與標準 JS。節號由「01 · Context」調整為「Context · 01」——字詞未增減，僅調換順序以符合標準的「標籤在前、數字在後」，同時讓正則解析得到。改版前後做過可見文字逐段 diff，34 處差異全部是新增的導覽 chrome 與節號順序，**教學內文未更動**。
**影響範圍：**
- `Unit_11/slides.html` — `:root` 色票、結構 class、頁首頁尾、圓點導航 JS
- `Unit_11/article.html` — CSS 全換、side-nav／refs／sec-title／tbl-wrap、標準 JS、節號順序

### 4. Unit_11/resources/常見標籤類型.md 與 sp-dp.md 內容完全重複
**狀態：** 已修復
**問題：** `Unit_11/resources/` 下兩份 `.md` 檔名不同，但內容一字不差，都是 Android SP／DP 單位的說明。依檔名判斷，`常見標籤類型.md` 原本應該放的是標籤類型的資料。
**原因：** 建立來源檔時複製貼上貼錯，兩個檔案都寫進了 SP／DP 的內容。
**佐證：**
```
$ md5 -q Unit_11/resources/sp-dp.md Unit_11/resources/常見標籤類型.md
（兩檔大小同為 1578 bytes，內容逐行比對一字不差，
  皆以「# **SP 與 DP 的差異**」開頭）
```
**修正：** 已由用戶於 2026-08-11 補上正確內容。現在是完整的 iOS 標籤規範：四種標籤類型（Large Title／Secondary／Body／Small Text）、SF Pro 的九列字級表（34／28／17／15／16／13／12／11pt 與對應粗細）、行高建議（字級的 1.2–1.4 倍）、邊距（上下 8–16pt、左右 16–20pt）與文字截斷原則。
```
$ md5 -q sp-dp.md 常見標籤類型.md
013c7983f794e3c9ee1a50cd9bd667ed
88e847363e1ca8331b07e421b7563d5a   → 已不相同（1578 vs 2368 bytes）
```
**待辦（不影響本筆狀態）：** 這份來源目前尚未被任何教材引用。查證後確認 `article.html` 與 `checklist.html` 命中的「SF Pro」是 CSS 字型堆疊而非內文；`slides.html` 只有一列 `17pt / 16sp` 的字級樣本，沒有完整字級表。若要讓這份來源真正發揮作用，適合放進講義 §8「文字與表單」與簡報第 15 張「文字系統需要回應縮放」。
**影響範圍：**
- `Unit_11/resources/常見標籤類型.md` — 內容已更新為 iOS 標籤規範（查證位置：全文與 md5 比對）
