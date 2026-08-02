# [SPEC] Unit 06 完整教材建置（Flowchart 到 Wireframe）

- **日期**：2026-08-02
- **負責人**：bryant_huang
- **狀態**：done
- **變更紀錄**：[docs/changelog/unit06-flow-wireframe.md](../changelog/unit06-flow-wireframe.md)

---

## 背景

Unit 06 對應資展時段 2026/08/03（一）13:30–16:30，主題為「介面設計流程（上）：Flowchart 到 Wireframe」。階段作業 5「Flowchart + UI Flow + Wireframe」橫跨 Unit 06–07，交件為 1 張 Flow + 3–5 個 Wireframe。

原 `Unit_06/slides.html` 是舊課綱的「十大易用性原則與檢查表實務」（14 張），README 註明「⚠️ 簡報 slides.html 尚未依新主題重製」，`index.html` 顯示「簡報準備中」。

與 Unit 05 不同的是，`Unit_06/resources/` **完全是空的**——沒有任何來源資料。依 `unit-materials` skill 的溯源原則不能自行編寫內容，因此先查證權威來源並整理成 `resources/guide.md`，再據此撰寫教材。

舊的十大易用性原則在新版課綱中已無對應單元，但內容本身可用，需要決定去處。

## 功能說明

三份互相串接的 HTML 教材，加上兩個 Figma 課堂練習檔。

**簡報 `slides.html`（26 張）**
封面 → 議程 → 這堂課在哪裡 → 四個常被混用的詞 → Journey vs Flow → Flowchart 與 Wireframe 各自的盲點 → Wireflow → 什麼時候用哪一種 → Flowchart 四個符號 → 一條流程要交代三件事 → 例外路徑六條 → 從 IA 到 Flow → Wireframe 在回答什麼 → 保真度三維度 → 低保真 vs 高保真 → 為什麼停在低保真 → 該放什麼不該放什麼 → 六題檢查清單 → Auto Layout 為什麼要用 → 三種排列方向 → Padding 與 Gap → Hug／Fill／Fixed → Constraints → 課堂練習 → 回家作業 → 延伸資源。

**講義 `article.html`（13 節）**
在簡報基礎上展開，含 Figma 快捷鍵表與三段可複製的 AI 協作提示詞（檢查流程缺口、從流程推出需要哪些畫面、檢查 Wireframe 資訊層級）。

**練習 `exercises.html`**
- 課堂練習 80 分鐘：拆步驟 15／畫 Flowchart 20／Auto Layout 練手 20／畫 3 個 Wireframe 25，另計 15 分鐘成果分享。
- 回家作業對應作業 5 上半，附 100 分配比（+5 加分項）與「不及格的樣子」對照欄。

**兩個 Figma 練習檔**
Auto Layout 是 design mode 功能、FigJam 不支援，因此拆成兩檔：FigJam 給 Exercise 01–02 的流程圖，Figma design 給 Exercise 03–04 的 Auto Layout 與 Wireframe。

## 實作範圍

- `Unit_06/resources/guide.md` 來源整理（NN/g 四篇 + Figma 官方兩篇，含課程對照）。
- `Unit_06/slides.html` 重製為 26 張，新增 `.flow-dia` 與 `.wf` 兩個元件。
- `Unit_06/article.html` 新建 13 節。
- `Unit_06/exercises.html` 新建課堂練習與回家作業。
- `Unit_06/README.md` 重寫，含三小時時間分配表。
- `index.html` Unit 06 卡片改為三個入口。
- 兩個 Figma 課堂練習檔建置與連結串接。
- 舊簡報移至 `Unit_09/usability-heuristics.html` 並改標。
- Codex 內容審查與修正。

## 不在範圍內

- **Wireflow 實作**：本單元只教觀念與適用時機，實際合成 Wireflow 留給 Unit 07。
- **第二條 Flow**：課綱交件規格是 1 張 Flow，因此作業只要求一條完整流程；第二條降為 +5 加分項。（初版誤加為必要項，經 Codex 指出後修正。）
- **每張 Wireframe 都做狀態版本**：改為整組至少涵蓋一個關鍵例外狀態。
- **Grid Auto Layout 實作**：講義列出三種排列方向，但練習只操作垂直與水平。
- **響應式與多斷點**：Constraints 只講「何時不用它」與 absolute position 例外，深入留給 Unit 09。
- **Unit_09 封面張數修正**：驗收腳本發現 `Unit_09/slides.html` 寫 21 張但實際 22 張，屬既有內容，未修改。

## 驗收條件

- [x] 簡報 26 張可正常翻頁，深色頁的翻頁按鈕與行內連結自動變亮色
- [x] 講義側邊大綱、閱讀進度條、提示詞複製按鈕運作正常
- [x] 三份 HTML 通過 `validate.py`：結構、id、連結、跨檔錨點、CSS class、編號全綠
- [x] 時間對帳一致：Agenda 50+35+95 = 180 分；課堂練習 15+20+20+25 = 80 分；評分配分 30+15+25+15+15 = 100（+5 加分）
- [x] 教材內容全部可溯源至 `resources/guide.md`，並經 Codex 對照審查
- [x] 作業要求與課綱作業 5 的交件規格一致（1 張 Flow + 3–5 個 Wireframe）
- [x] 兩個 Figma 練習檔已建立，素材與空白畫框備妥，連結接回四份教材
- [x] 舊的十大易用性原則已移至 Unit_09 並改標，未直接刪除
- [x] `index.html` Unit 06 卡片提供簡報／講義／練習與作業三個入口
