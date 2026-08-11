# [LOG] Unit 11 APP UI 設計規範教材與自我檢核表

對應規格：[docs/spec/unit11-app-ui.md](../spec/unit11-app-ui.md)

---

## 2026-08-11 — 簡報與講義對標現行版型

**修改檔案：**
- `Unit_11/slides.html` — `:root` 色票、結構 class、頁首頁尾、圓點導航 JS
- `Unit_11/article.html` — CSS 全換、side-nav／refs／sec-title／tbl-wrap、標準 JS

**實作說明：**

動手前先確認另一個工作階段已經收工（檔案 10 秒內無變動、Codex session transcript 停止成長），避免與正在寫入的程序衝突。

**簡報換皮。** 色票整組換成標準色，與 `Unit_10/slides.html` 逐項比對後 9 個共用 token 完全一致。平台區分依用戶選擇映射到標準色：iOS→`--accent` 藍、Android→`--accent2` 綠、警告→`--accent3` 橘。結構 class 對齊 `slide-head`／`unit-pill`／`slide-num`／`slide-body`／`slide-foot`／`cover-eyebrow`／`cover-sub`／`course-label`，id 對齊 `#prog`／`#ctrls`。

改名時有個坑：`.body` 這個 class 與 `body` 元素選擇器同名，用帶點前綴的比對（`\.body\b`）只改 class，`html, body { }` 那條保持完好。

頁尾原本是兩個 `.course` 標語欄，第二個換成圓點導航（22 張全部），並補上深色頁的圓點與翻頁按鈕反白。保留固定 1920×1080 畫布縮放、`localStorage` 記憶頁碼、分頁標題跟著投影片變這三項本單元特有的機制。手機模型、Safe Area、觸控目標等平台示意圖只換色票，比例未動。

**講義換皮。** CSS 換成 `Unit_08/article.html` 的標準版，補上 `side-nav`（從既有 TOC 項目生成）、`refs`（原 `.sources` 移出 `.article` 並改名）、10 個 `sec-title`、6 處 `tbl-wrap`，JS 換成標準版（捲動進度、`IntersectionObserver` 大綱高亮）。

節號由「01 · Context」調整為「Context · 01」——`validate.py` 第 142 行的正則 `[^<\d]*(\d+)\s*</p>` 只容許數字前面有標籤（Unit_03 的「SECTION 01」是這個格式），數字後面還有字會解析不到。調換順序後字詞未增減，也符合標準的「標籤在前、數字在後」。

改版前後做過可見文字的逐段 diff：34 處差異全部可解釋——12 處是新增的側邊大綱與「參考資料」標題，20 處是節號順序調換，1 處是返回連結由「← Unit 11 簡報」改為「回到投影片」（箭頭改由 CSS `::before` 產生，避免重複；用字對齊其他 7 個單元的慣例）。**教學內文一個字都沒動。**

---

## 2026-08-11 — 新增 APP 介面自我檢核表

**修改檔案：**
- `Unit_11/checklist.html` — 8 組 29 項互動檢核表（新增）
- `Unit_11/article.html` — foot-nav 與第 10 節加互動版入口
- `Unit_11/slides.html` — 資源頁加入口
- `Unit_11/README.md`、`index.html` — 教材入口與卡片三入口

**實作說明：**

項目依講義 10 節的實際教學內容展開成 8 組 29 項：平台與慣例 3、單位與畫布 4、安全區域 3、導覽 4、觸控與回饋 5、文字與表單 4、無障礙 3、交件檢查 3。每組標題旁有回對應章節的連結，10 個錨點全部驗證有效。

每一項有三層資訊：檢查標題、判斷依據（含 `44×44 pt`、`48×48 dp`、`4.5:1` 等實際數字）、常見未達成情形。第三層是刻意設計的——只寫「觸控目標要夠大」學生會直接打勾，寫出「右上角關閉鍵只有 20×20，手指按三次才中一次」才會回去實測。

互動功能參考 `Unit_09/usability-heuristics.html` 既有的檢核表模式，並擴充：`localStorage` 保存勾選、整體與分組雙層進度、只看未完成過濾（`body.only-todo` + `:has()`）、`@media print` 列印排版（隱藏工具列、項目不跨頁斷開）、可複製的純文字結果摘要供貼進作業說明。

樣式沿用剛對標好的標準講義系統，另加檢核表專用元件，無使用但未定義的 class。

**語氣調整（用戶要求）：** 依專案慣例改為陳述句——移除全部第二人稱（「你」歸零）、把 30 則情緒化進度文案（「找到問題就是進度」「再一下就好」）整個陣列刪除，改成依狀態產生的三種中性敘述（尚未開始檢核／尚有 N 項未通過／全部項目均已通過）、「沒過的樣子」改為「常見未達成情形」、唯一一處命令式的項目說明（「不要用眼睛判斷」）改為「不以目視判斷」。改完 JS 重新通過 `node --check`。

**已知問題 / 備註：**

`Unit_11/resources/常見標籤類型.md` 與 `sp-dp.md` 內容完全重複，見 [future/maintain.md](../../future/maintain.md) 2026-08-11 第 4 筆，狀態未修復。

`Unit_11/resources/App 設計.pdf` 有 3.1 MB，是本單元的來源依據所以依溯源原則保留。若日後 repo 大小成為問題，這是第一個可以考慮抽出的檔案。
