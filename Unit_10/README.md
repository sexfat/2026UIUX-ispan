# 單元 10：UI 設計精度提升：Mockup 細節
> 對應資展時段：2026/08/10（一）13:30–16:30

## 相關檔案

- `slides.html` — 課堂簡報（22 張）。
- `article.html` — 完整教材（11 節）。
- `exercises.html` — 課堂練習四階段與回家作業（作業 8）。
- `resources/guide.md` — 十大易用性原則的來源整理與圖片對照表。
- `resources/heuristics/` — 16 張案例圖片，取自 71NEXT 該篇文章內嵌的圖。

## 時間分配（3 小時 / 180 分鐘）

| 段落 | 時間 |
| :--- | :--- |
| Part 1 · 精度差在哪 | 25 分 |
| Part 2 · 十大易用性原則 | 40 分 |
| 休息 | 15 分 |
| Part 3 · 課堂練習 | 85 分 |
| Part 4 · 成果分享 | 15 分 |

課堂練習四階段：補狀態 20 分 → 十條逐條檢查 25 分 → 改稿並標註 25 分 → 兩人互相檢查 15 分。

## 單元目標

- 能把 Wireframe 升級為高保真 Mockup，並說得出精度差在哪三件事。
- 能讓畫面上的間距全部落在風格板的階梯上，並用 Figma 量測驗證。
- 能用 Component 與 Variants 管理元件狀態，而不是複製貼上五顆按鈕。
- 能用真實內容取代假字，並在版面爆掉時回頭修元件。
- 能拿十大易用性原則逐條檢查介面，寫出「違反第幾條、在哪個位置、怎麼改」。

## 課程介紹

這個單元進入高保真 Mockup。前面單元已經給了材料：Unit 08 的風格板決定了色彩、字級與間距基準，Unit 09 的多斷點版面決定了結構，Unit 07 畫過空狀態、錯誤狀態與載入狀態。這堂課的重點是把它們執行到底。

把風格板的顏色套上去，畫面會變好看，但它還是一張 Wireframe——判斷標準是：這張圖交給工程師後，能不能不補問就開始做。不夠的部分幾乎永遠是同樣三件事：間距沒有真的照基準單位用、每個可互動元件只畫了一種狀態、內容還停在 Lorem ipsum。

後半段導入十大易用性原則。這是 Jakob Nielsen 在 1994 年整理出來的十條檢查原則，用途是把「怪怪的但說不出來」變成「違反第 5 條，刪除沒有二次確認」。它不會決定按鈕該放哪，但它會讓問題可以被說出口、被排序、被修掉。

## 課程內容

- Mockup 精度三件事：間距與對齊、狀態、真實內容。
- 在 Figma 量間距（Option 鍵）、用 Component 與 Variants 管理狀態。
- 十大易用性原則逐條講解，每一條配真實介面案例圖。
- 把十條收成一張可以直接對著畫面問的檢查表。
- AI 輔助：產生真實感假資料、改寫介面文案與錯誤訊息、比對狀態缺漏。

## 對應資展日期與時段

- 2026/08/10（一）下午 13:30–16:30
- 課程總覽主題：UI 設計精度提升：Mockup 細節

## 本單元產出

- 對應 `資展課程大綱.md` 第五節階段作業表：
- 作業 8：高保真 Mockup（主要頁面），本單元完成 1–2 個主要頁面的高保真版本，附十條檢查紀錄與互檢修正清單。

## 十大易用性原則（本單元 Part 2）

| # | 中文標題 | English |
| :-- | :--- | :--- |
| 1 | 系統狀態的可見性 | Visibility of System Status |
| 2 | 連結真實世界 | Match Between System and the Real World |
| 3 | 讓使用者有控制權及自由度 | User Control and Freedom |
| 4 | 一致性與標準 | Consistency and Standards |
| 5 | 預防錯誤 | Error Prevention |
| 6 | 用認知方式而非記憶 | Recognition Rather Than Recall |
| 7 | 具備使用靈活性和效率 | Flexibility and Efficiency of Use |
| 8 | 設計美觀與極簡 | Aesthetic and Minimalist Design |
| 9 | 易於使用的錯誤處理和回饋 | User-Friendly Error Handling and Feedback |
| 10 | 教學指示與幫助 | Help and Documentation |

順序與中文標題依 71NEXT 該篇整理，逐條原句抄錄在 `resources/guide.md`。

## 參考資料

- [使用者介面設計的10大易用性](https://www.71next.com/userDoc/10-usability-heuristics/) — 71NEXT。本單元十條的中文標題、原則說明、Tips 與案例圖片的來源。
- [10 Usability Heuristics for User Interface Design](https://www.nngroup.com/articles/ten-usability-heuristics/) — NN/g，Jakob Nielsen 1994 年的原始版本，附官方海報下載。
- [Usability Heuristics Applied to Virtual Reality](https://www.nngroup.com/articles/usability-heuristics-virtual-reality/) — NN/g，同一組原則套用到 VR。
- [10 Usability Heuristics Every Designer Should Know](https://uxdesign.cc/10-usability-heuristics-every-designer-should-know-129b9779ac53) — UX Collective。
- [Guide to components in Figma](https://help.figma.com/hc/en-us/articles/360038662654-Guide-to-components-in-Figma) — 主元件與實例、覆寫與重設。
- [Create and use variants](https://help.figma.com/hc/en-us/articles/360056440594-Create-and-use-variants) — 用變體管理元件狀態。
- [Material Design 3 — Grids & spacing](https://m3.material.io/foundations/layout/grids-spacing/spacing) — 間距系統的完整範例。
- [WCAG 2.2 — Contrast (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) — 停用狀態調淡時要顧的對比度門檻。

## 圖片使用說明

`resources/heuristics/` 的 16 張圖是 71NEXT 該篇文章內嵌的案例圖（多數為 Behance、Pinterest、Dribbble、Medium 的外部連結），下載保存是為了課堂教材能離線播放。**僅供課堂教學引用，學生作品集不可沿用。** 每張圖的原始網址與對應條目列在 `resources/guide.md` 的圖片對照表。
