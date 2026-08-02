# 單元 6：介面設計流程（上）：Flowchart 到 Wireframe
> 對應資展時段：2026/08/03（一）13:30–16:30

## 相關檔案

- `slides.html` — 課堂簡報（26 張）。
- `article.html` — 完整教材（13 節，含 Figma 操作與 AI 協作提示詞）。
- `exercises.html` — 課堂練習（四階段）與回家作業（作業 5 上半）。
- `resources/guide.md` — NN/g 與 Figma 官方文件的中文整理，本單元教材的溯源依據。
- 課堂練習檔 ①：[FigJam · 流程圖](https://www.figma.com/board/80weQpwuu9BGHrlos8Emhy)（符號庫、動作便利貼、例外路徑檢查表）。
- 課堂練習檔 ②：[Figma · Auto Layout 與 Wireframe](https://www.figma.com/design/3rw5NBkNFX2ZOHvJGXS2Mt)（卡片素材、3 個空白畫框、六題檢查清單）。

## 單元目標

- 能分辨 User Journey、User Flow、Flowchart、Wireflow 的差別，並知道什麼情況該用哪一種。
- 能把資訊架構轉成任務流程，標出判斷點與例外路徑。
- 能建立低保真 Wireframe，聚焦結構、層級與操作順序。
- 理解原型保真度的三個維度，並說明為什麼這個階段要停在低保真。
- 能用 Figma Auto Layout 建立可調整的版面骨架，並分辨 Auto Layout 與 Constraints 的分工。

## 課程介紹

這個單元開始從研究文件進入介面骨架。Unit 05 交出來的 IA 圖像是一張捷運路線圖：看得到有哪些站、怎麼轉乘，但沒告訴任何人「從家裡到公司該怎麼走」。那條路線就是這堂課要畫的 Flow。

Flowchart 用來描述邏輯與分支，Wireframe 則把流程轉成初步版面，先處理資訊順序與操作關係。Wireframe 階段不追求視覺精緻——一旦上了色，評圖的回饋就會全部集中在配色與字體，結構問題被掩蓋，等到 Mockup 才發現要重畫的量是現在的十倍。因此本單元刻意限定黑白灰。

Figma Auto Layout 放在 Wireframe 製作脈絡下教。透過水平、垂直容器、Padding、Spacing 與 Resizing，可以更快建立可調整的卡片、列表與表單骨架，讓後續版面變動不必重畫。

## 課程內容

- 四個常被混用的詞：User Journey、User Flow、Flowchart、Wireflow 的差別與適用時機。
- Flowchart：四個符號、判斷點寫法、入口／判斷點／終點三件事。
- 例外路徑六種：沒資料、找不到、沒權限、出錯、要等、反悔。
- 從 IA 圖轉成 Flow 的四個步驟。
- Wireframe：該放什麼、不該放什麼、畫完的六題檢查清單。
- 保真度的三個維度（互動、視覺、內容）與低／高保真的取捨。
- Figma Auto Layout：三種排列方向、Padding 與 Gap、Hug／Fill／Fixed 三種尺寸模式。
- Constraints 與 Auto Layout 的分工，以及 absolute position 的使用時機。

## 課堂練習

**從 IA 圖畫到 3 個 Wireframe**（80 分鐘，個人作業，Figma／FigJam）

1. 挑一條路徑，拆成使用者的動作（15 分）— 從 IA 圖挑一條核心路徑，動詞開頭寫成便利貼。
2. 畫成 Flowchart，補上例外路徑（20 分）— 四個符號，逐一核對六種例外狀況。
3. Auto Layout 練手（20 分）— 做一張會自己撐開的卡片、一個會跟著容器縮放的列表，並刻意踩一次 Hug／Fill 衝突的坑。
4. 畫 3 個低保真 Wireframe（25 分）— 涵蓋流程的頭、中、尾。第 1 張用 Auto Layout 做完整，另 2 張先排骨架，畫完逐張回答六題檢查清單。

之後另有 15 分鐘成果分享與作業說明（抽點 3–4 位，每人 3 分鐘）。

產出：1 張 Flowchart + 3 個 Wireframe + Auto Layout 卡片與列表。

### 三小時時間分配

| 段落 | 時間 | 內容 |
| :--- | :--- | :--- |
| Part 1 | 50 分 | 四種流程圖的差別、什麼時候用哪一種、Flowchart 畫法、例外路徑 |
| Part 2 | 35 分 | Wireframe 在回答什麼、保真度三維度、該放什麼不該放什麼 |
| Part 3 | 95 分 | Figma 實作 80 分 + 成果分享與作業說明 15 分 |

## 回家作業

**作業 5（上半）：完整流程與 3–5 個 Wireframe**

1. 把課堂上那條 Flowchart 補完整，六種例外路徑一條都不能少，圖上不能有斷掉的箭頭。
2. Wireframe 補到 3–5 個畫面，整組至少涵蓋一個關鍵的例外狀態（空狀態或錯誤狀態）。
3. 每張 Wireframe 旁邊寫下六題檢查清單的答案。
4. 交件前做 Auto Layout 壓力測試：主要容器拉寬 1.5 倍、縮到 0.7 倍、標題改成兩倍長，確認不爆版。
5. （加分，非必要）畫第二條會與第一條交會的 Flow，交會點要畫出來，完成後要回得到原位置。

交件規格對齊課綱作業 5：**1 張 Flow + 3–5 個 Wireframe**。

## 對應資展日期與時段

- 2026/08/03（一）下午 13:30–16:30
- 資展時程主題：【實務】介面設計流程（上）：市場研究產品、Flowchart、UI flow、Wireframe、Mockup 設計流程

## 本單元產出

- 對應 `資展課程大綱.md` 第五節階段作業表：
- 作業 5：Flowchart + UI Flow + Wireframe，與 Unit 07 共同完成；本單元先產出 Flow 與初版 Wireframe，Unit 07 細修並合成 Wireflow。

## 參考資料

- [Wireflows: A UX Deliverable for Workflows and Apps](https://www.nngroup.com/articles/wireflows/) — NN/g，Wireflow 定義與實作準則。
- [User Journeys vs. User Flows](https://www.nngroup.com/articles/user-journeys-vs-user-flows/) — NN/g，兩種尺度的定義與對照。
- [UX Prototypes: Low Fidelity vs. High Fidelity](https://www.nngroup.com/articles/ux-prototype-hi-lo-fidelity/) — NN/g，保真度三維度與取捨。
- [UX Deliverables: Glossary](https://www.nngroup.com/articles/ux-deliverables-glossary/) — NN/g。
- [Guide to auto layout](https://help.figma.com/hc/en-us/articles/360040451373-Guide-to-auto-layout) — Figma 官方文件。
- [Apply constraints to define how layers resize](https://help.figma.com/hc/en-us/articles/360039957734-Apply-constraints-to-define-how-layers-resize) — Figma 官方文件。

## 備註

- 原 `Unit_06/slides.html`（十大易用性原則與檢查表實務，14 張）已移至 `Unit_09/usability-heuristics.html` 作為延伸教材，並改標為 Unit 09。該主題在新版課綱中已無對應單元。
