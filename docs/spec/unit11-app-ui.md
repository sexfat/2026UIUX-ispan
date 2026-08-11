# [SPEC] Unit 11 APP UI 設計規範教材與自我檢核表

- **日期**：2026-08-11
- **負責人**：bryant_huang
- **狀態**：done
- **變更紀錄**：[docs/changelog/unit11-app-ui.md](../changelog/unit11-app-ui.md)

---

## 背景

Unit 11「APP UI 設計規範」的簡報與講義由另一個工作階段獨立建置，內容完整但沒有沿用 `unit-materials` skill 的對標規則：色票、結構 class、元件命名都跟 Unit 03–10 不同，從首頁點進去風格明顯斷裂；講義另缺 `side-nav` 與 `refs`，`validate.py` 報三個錯。

此外，講義第 10 節的 APP 介面檢核表只有 8 個粗略項目、且是靜態的，學生看過就忘，也無法留下可交件的檢核紀錄。

## 功能說明

1. **簡報與講義對標現行版型**——色票、結構 class、頁首頁尾與導覽行為統一到課程標準，同時保留本單元特有且堪用的機制（固定 1920×1080 畫布、`localStorage` 記憶頁碼、分頁標題跟著投影片變）與平台示意圖。
2. **新增可勾選的自我檢核表**——`checklist.html`，8 組 29 項對應講義 10 個章節，作為作業 9 交件前的檢核工具。

## 實作範圍

- `Unit_11/slides.html`：色票、結構 class、圓點導航、深色頁按鈕反白。
- `Unit_11/article.html`：標準 CSS、`side-nav`、`refs`、`sec-title`、`tbl-wrap`、標準 JS。
- `Unit_11/checklist.html`：8 組 29 項互動檢核表（新增）。
- `Unit_11/README.md`、`index.html`：教材入口與卡片三入口。

## 不在範圍內

- 簡報不改為流動版型——固定 1920×1080 畫布是本單元的既有設計，改成 `clamp()` 等於 22 張投影片版面重排，平台示意圖的比例會跑掉（已與用戶確認採「換皮」而非「連版型一起改」）。
- 講義與簡報的教學內文不更動。
- 深淺頁分布維持原編排（6 張深色、3 張 Android 綠底），那是內容節奏不是樣式。
- 練習頁（`exercises.html`）未建置。

## 驗收條件

- [x] 簡報色票與 Unit_10 逐項比對一致（共用 token 全數相同）
- [x] 講義色票與 Unit_08 講義完全一致
- [x] 改版前後可見文字逐段 diff，差異僅為新增導覽 chrome 與節號順序
- [x] 檢核表 8 組分母與實際項數一致，10 個講義錨點全部有效
- [x] 檢核表無使用但未定義的 class，JS 通過 `node --check`
- [x] `validate.py Unit_11` 全綠
