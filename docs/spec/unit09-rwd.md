# [SPEC] Unit 09 完整教材建置（響應式網頁設計 RWD）

- **日期**：2026-08-11
- **負責人**：bryant_huang
- **狀態**：done
- **變更紀錄**：[docs/changelog/unit09-rwd.md](../changelog/unit09-rwd.md)

---

## 背景

`index.html` 定義 Unit 09 為「Web 設計規範與網頁結構」，2026/08/10（一）09:00–12:00。但 `Unit_09/slides.html` 是舊課綱的「完形心理學與 Laws of UX」，README 註明尚未依新主題重製，首頁顯示「簡報準備中」。

RWD 的完整教材原本放在 master 分支的 Unit_12，但現行課綱的 Unit 12 已改為作品展與專題發表，不安排課程簡報。這份 RWD 內容需要搬到正確的單元。

## 功能說明

16 張投影片的響應式網頁設計教材：

1. **RWD 概念與五種版面模式**——Mostly Fluid、Column Drop、Layout Shifter、Tiny Tweaks、Off Canvas，各附線上示範連結。
2. **斷點設置**——四個常見區間、Desktop First 與 Mobile First 的 Media Query 差異。
3. **響應式表格與圖片**——表格四種策略、圖片六種處理方式。
4. **RWD vs AWD**——運作方式、版面切換、維護成本、客製化程度的比較，附可現場驗證的實例。
5. **核心概念**——流動性、相對單位、斷點設計、巢狀容器，各配 Froont 原始動圖。
6. **Figma 多裝置設計**——Frame、Constraints、Auto Layout 三步驟，附 Figma 練習檔。

## 實作範圍

- `Unit_09/slides.html`：16 張簡報，內容逐字取自 master 分支的 Unit_12。
- `Unit_09/resources/originals/`：Froont 文章的 9 支原始 GIF。
- `Unit_09/README.md`：RWD 核心概念整理、課堂練習連結、RWD vs AWD 實測對照表。
- `index.html`：Unit 09 卡片入口與 Figma 練習檔按鈕。

## 不在範圍內

- 不更動 master 分支（該分支全程保持乾淨）。
- 不重寫內容順序或文字，僅換色票與單元標記。
- 講義與練習頁未建置（本單元目前只有簡報）。

## 驗收條件

- [x] 16 張投影片，內容順序與 master 版 Unit_12 一致
- [x] 綠色系色票全部映射為課程標準藍，無舊色字面值殘留
- [x] 9 支 Froont 動圖下載保存並嵌入對應段落
- [x] RWD vs AWD 的示範網站經實測確認行為成立
- [x] `validate.py Unit_09` 全綠
