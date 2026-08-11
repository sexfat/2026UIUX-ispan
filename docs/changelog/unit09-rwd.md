# [LOG] Unit 09 完整教材建置（響應式網頁設計 RWD）

對應規格：[docs/spec/unit09-rwd.md](../spec/unit09-rwd.md)

---

## 2026-08-10 — 換成 RWD 主題並套用現行簡報版型

**修改檔案：**
- `Unit_09/slides.html` — 16 張 RWD 簡報（整份取代舊的完形／Laws of UX 內容）
- `Unit_09/README.md` — 改為 RWD 核心概念整理
- `index.html` — Unit 09 卡片改為可點的簡報連結

**實作說明：**

用 `git archive master Unit_12 | tar -x` 把 master 分支的 Unit_12 取出到暫存目錄，不切換分支、不動 master。內容逐字複製，順序與文字全部不動，只做兩件事：

- 身分標記：`Unit 12` → `Unit 09`，`WEB UI & UX 實務` → `Web 設計規範與網頁結構`。
- 色票：原檔是綠色系（`--accent: #5c9e3e`），整組映射到課程標準藍。九階對應為 `#5c9e3e`→`#0066cc`、`#6ab048`→`#1a7fe0`、`#8fc46a`→`#5aa8ea`、`#b8d9a0`→`#a9cdf2`、`#c6ddb0`→`#bdd8f5`、`#d4e8c6`→`#d6e7fb`、`#3d6b2a`→`#0a4f9e`、`#2d5a1e`→`#073a73`、`#1a3812`→`#04264d`，以及所有 `rgba(92,158,62,…)`→`rgba(0,102,204,…)`。裝置示意圖裡代表不同區塊的紅色與紫色不是品牌色，維持原樣。

原本先做過一次「套用 Unit_08 版型」的重製（改用 `.cmp-table`／`.matrix` 等標準元件），但用戶要求改為完全照 master 內容不動順序，因此回退成逐字複製 + 換色的做法。

**已知問題 / 備註：**

`slide-num` 是寫死的（舊版寫法），`validate.py` 會提示但不算錯誤。若日後要改為 JS 自動編號，需連同 16 張的分母一起處理。

---

## 2026-08-10 — 換上 Froont 原始動圖並補上 Figma 練習連結

**修改檔案：**
- `Unit_09/slides.html` — 8 處示意圖改為動態 GIF、`.ref-img` 樣式、第 14 張練習連結
- `Unit_09/resources/originals/*.gif` — 9 支動圖（新增）
- `Unit_09/README.md` — 課堂練習區塊
- `index.html` — Unit 09 卡片加 Figma 練習檔按鈕

**實作說明：**

`resources/originals/` 原本已有 9 張靜態 PNG，檔名與 blog.froont.com〈9 Basic Principles of Responsive Web Design〉的圖一一對應，但那是截圖版。從原文抓下 9 支原始 GIF（1100×400，版本 89a）取代，流動性、相對單位、斷點、巢狀容器、字型與圖示等段落改為動態示意，比靜態圖更能說明「螢幕變窄時發生什麼事」。

`.ref-img` 依用戶要求移除白底與外框，只留圓角，讓動圖融進投影片背景。

第 15 張參考資源補上 Froont 原文連結，標明這幾張示意圖的出處。

`max-min-width.gif` 也下載了，但目前 16 張投影片沒有對應的專屬頁面（原本第 10 張只在說明文字提過 max-width），保留在 resources 備用。

---

## 2026-08-11 — RWD vs AWD 改用實測得出的範例

**修改檔案：**
- `Unit_09/slides.html` — 第 8 張的比較表欄位與現場驗證說明
- `Unit_09/README.md` — 新增實測對照表

**實作說明：**

詳見 [future/maintain.md](../../future/maintain.md) 2026-08-11 第 1 筆。原本沿用舊教材的 PChome（RWD）與 momo（AWD）實測不成立，改為 591（AWD，手機 UA 會轉到 `m.591.com.tw`）與台灣高鐵（RWD，兩種 UA 的 HTML byte-identical）。

**已知問題 / 備註：**

網站會改版，這是 2026/08/10 的實測結果。簡報與 README 兩處都已加註「上課前建議再開一次確認」。
