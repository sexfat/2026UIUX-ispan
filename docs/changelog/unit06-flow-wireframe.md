# [LOG] Unit 06 完整教材建置（Flowchart 到 Wireframe）

對應規格：[docs/spec/unit06-flow-wireframe.md](../spec/unit06-flow-wireframe.md)

---

## 2026-08-02 — 建置三份教材、兩個 Figma 練習檔，並依 Codex 審查收斂作業範圍

**修改檔案：**
- `Unit_06/resources/guide.md` — 來源整理（新增）
- `Unit_06/slides.html` — 26 張投影片（由舊主題「十大易用性原則」重製）
- `Unit_06/article.html` — 13 節長文教材（新增）
- `Unit_06/exercises.html` — 課堂練習與回家作業（新增）
- `Unit_06/README.md` — 重寫，含三小時時間分配表與參考資料
- `Unit_09/usability-heuristics.html` — 由 `Unit_06/slides.html` `git mv` 移入，unit pill 與 course-label 改標為 Unit 09
- `index.html` — Unit 06 卡片由「簡報準備中」改為三個入口

**實作說明：**

*溯源：先建立來源，再寫教材*
`Unit_06/resources/` 原本是空的。依 skill 的溯源原則，先查證權威來源並整理成 `resources/guide.md`：NN/g 的 Wireflows、User Journeys vs User Flows、UX Prototypes 低高保真、UX Deliverables Glossary，加上 Figma 官方的 Guide to auto layout 與 Constraints 文件。每個段落標出處並附「課程對照」，讓後續維護仍有依據。

*教學框架*
把四個常被混用的詞整理成「前兩個是尺度、後兩個是畫法」：User Journey 與 User Flow 是尺度差異（Journey 是 Unit 04 做過的），Flowchart 與 Wireflow 是把 Flow 畫出來的兩種格式。並在講義註明這是課堂上的整理法，不是業界唯一分類。

例外路徑設計成六條固定檢查表（沒資料、找不到、沒權限、出錯、要等、反悔），貫穿簡報、講義、練習頁與 Figma 板，讓學生有一個可以逐條核對的清單。

*Figma 練習檔：為什麼是兩個*
Auto Layout 是 design mode 的功能，FigJam 不支援，因此拆成兩檔：
- **①（FigJam）** `https://www.figma.com/board/80weQpwuu9BGHrlos8Emhy` — 四區塊：使用說明（使用者目標與入口填空）／Exercise 01 動作便利貼區（附寫法對照）／Exercise 02 流程符號庫（起訖、動作、判斷點、例外四個現成元件）+ 工作區／例外路徑六條檢查卡。
- **②（Figma design）** `https://www.figma.com/design/3rw5NBkNFX2ZOHvJGXS2Mt` — 使用說明（規則與快捷鍵）／Exercise 03 素材區（縮圖、標題、說明、標籤四個零件**刻意不組起來**，四個步驟含故意踩 Hug／Fill 衝突那一關）／Exercise 04 三個空白畫框 + 六題檢查清單。

*Codex 審查修正*
以 `codex exec` 對照 `resources/guide.md` 審查，修正以下項目：

1. **作業範圍超出來源（最嚴重）**：課綱寫「1 張 Flow + 3–5 個 Wireframe」，初版卻要求第二條 Flow、且每張 Wireframe 都要有狀態版本。這是憑感覺加碼，違反溯源原則。第二條 Flow 降為 +5 加分項，狀態改為「整組至少涵蓋一個」，作業時數 4 小時 → 3 小時。
2. Flowchart 起訖符號描述為「圓角矩形」但圖上畫成 ◯，已註明正式畫法與課堂簡化畫法。
3. 成果分享寫「每人 3 分鐘」但 15 分鐘除不完，改為抽點 3–4 位。
4. 25 分鐘畫 3 張全 Auto Layout 不切實際，改為第 1 張做完整、第 2、3 張排骨架。
5. 補上 min／max width 的使用時機、桌機「只畫變動區塊」的操作規則、Constraints 垂直方向、高保真「設計師可專心觀察、減少人工操作失誤」兩個測試面向。
6. AI 提示詞在講義與練習頁重複，練習頁改為連回講義。
7. 評分「狀態完整度」定義模糊，改為「整組至少一張畫出狀態，並在流程圖上找得到對應的那條線」。

*未採納的建議*
Codex 建議把「現在畫得越醜，後面改得越輕鬆」「高保真真正的成本不是工時，是你捨不得改」改得更中性。這兩句是簡報上老師會直接講的話，改完會變成企業簡報口吻，與 `tone.md` 的「講課」要求衝突，因此保留。但「多數人第一次做，六條會漏掉四條」這種沒有根據的數字斷言已改掉，「交出去一問就露餡」也改為不那麼訓話的說法。

**已知問題 / 備註：**
- **一次回報錯誤**：套用 Codex 修正時，`cd Unit_06 && python3` 因 shell 當時已在該目錄而失敗，整段腳本沒有執行，但當時誤讀輸出、向用戶回報「已修正」。實際上 slides 與 article 有生效、exercises 與 README 沒有。已用絕對路徑重做並逐項驗證。**教訓：多檔案批次修改後要 grep 驗殘留，不要只看腳本的 print。**
- FigJam 的 section 子節點使用相對座標（沿用 Unit 05 的既有經驗，這次一開始就扣掉 section.x，未再出錯）。
- Unit_09 的十大易用性原則目前未從 `Unit_09/README.md` 或首頁連結，只是檔案存在。若要正式納入 Unit 09 教材需另外處理。
- 驗收腳本發現 `Unit_09/slides.html` 封面寫「21 張投影片」但實際 22 張，屬既有內容，**尚未修正**。
