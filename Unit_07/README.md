# 單元 7：介面設計流程（下）：Wireframe 實作延伸
> 對應資展時段：2026/08/06（四）09:00–12:00

## 相關檔案

- `slides.html` — 課堂簡報（25 張）。
- `article.html` — 完整教材（13 節，含 AI 協作提示詞）。
- `exercises.html` — 課堂練習（四階段）與回家作業（作業 5 下半）。
- `resources/guide.md` — NN/g 五組來源的中文整理，本單元教材的溯源依據。
- 課堂範本檔：[Unit 07 · 狀態設計與 Wireflow 練習範本](https://www.figma.com/design/X0nEWewUts2YSRElqN6dE3)（① 狀態盤點表 ② 三種狀態範本 ③ 標註格式 ④ 修正紀錄表，各對應課堂練習一個階段；學生複製區塊到自己的檔案填寫）。
- 作業題目卡：同檔案的[「作業題目」分頁](https://www.figma.com/design/X0nEWewUts2YSRElqN6dE3?node-id=6-2)，三題各含情境、Persona、必須畫出的狀態、容易踩的坑、交件清單與五個空白畫框：
  - 題目 1 · 會員註冊與登入（Unit 06 練過的基準題）
  - 題目 2 · 結帳付款出錯（本單元新出，主題為錯誤狀態的四種層級）
  - 題目 3 · 中途離開與返回（本單元新出，主題為五種往回的方式）
- Unit 06 的 Wireflow 與保真度來源整理在 `../Unit_06/resources/guide.md`，本單元第 7 節沿用。
- 線框元件庫：[Wireframe Web UI Kit](https://www.figma.com/design/XKrTQ38VaU4PZeuwT0uocp/Wireframe_Web_UI_Kit-%E5%88%87%E7%89%88%E7%9A%84100%E7%A8%AE%E7%B7%B4%E7%BF%92?node-id=0-1)（Unit 06 沿用，補畫狀態畫面時可直接取用現成區塊）。

## 單元目標

- 能分辨空狀態、錯誤狀態、載入狀態三種畫面，並依準則各畫出一張。
- 能寫出同時做到明確、看得懂、有禮貌、精準、給下一步的錯誤訊息。
- 能依等待時間（1 秒／2–10 秒／10 秒以上）選對進度指示的型別。
- 能分辨指示器、驗證、通知三種溝通方式，不互相誤用。
- 能把散裝 Wireframe 接成一張沒有斷點的 Wireflow，並寫出可執行的標註。
- 能主持與參與一場設計檢核：界定範圍、把個人偏好改寫成對著目標的提問、並在事後留下修正紀錄。

## 課程介紹

上一堂交出來的是一張 Flowchart 加三個 Wireframe，畫的是最順的那一條路——列表上有十幾筆資料、表單每格都填好、資料瞬間出現、使用者一路往前沒有回頭。這堂課把它補成真的能用的東西。

Unit 06 的六種例外路徑在這裡會被畫成真的畫面：「沒資料」與「找不到」變成空狀態，「出錯」與「沒權限」變成錯誤狀態，「要等」變成載入狀態，「反悔」變成「回到上一頁而且已填內容還在」。一個 Flowchart 上的菱形，通常會展開成兩三張長得不一樣的畫面。

畫面補齊之後，才有東西可以接成 Wireflow。接完再寫標註——時間、條件、規則、動態行為這四類東西怎麼畫都畫不出來，只能用文字寫。

最後一段是同儕檢核。設計檢核不是打分數，是判斷一份設計有沒有達成它自己設定的目標。學生要學會兩件事：被問的時候指得出決策的研究依據，以及問別人的時候把「我覺得這樣不好」改寫成對著目標的提問。檢核結束後留下的修正紀錄，就是下一版的工作清單。

這個階段仍然不上色。顏色與視覺風格留到 Unit 08 的風格板。

## 課程內容

- 三種必畫的狀態：空狀態、錯誤狀態、載入狀態，以及 Unit 06 六種例外路徑的對應關係。
- 空狀態三條準則：講清楚系統狀態、教功能怎麼用、給一條直達關鍵任務的路；以及「還沒有」與「找不到」的文案差別。
- 錯誤訊息的五要件：明確、看得懂、有禮貌、精準、給下一步。
- 表單錯誤回報十條準則：五條該做、五條不要做。
- 回應時間三門檻（0.1 秒／1 秒／10 秒）與進度指示的三種型別。
- 指示器、驗證、通知的分工與誤用代價。
- Wireflow 合成的四條準則，以及斷點的檢查方法。
- 標註的五種類型與寫法，含「刻意不做的事」。
- 設計說明：把版面決策接回 Unit 03–05 的研究產出。
- 設計檢核：三個前提、四種角色、回饋改寫；critique 與 review 的差別、五個常見失敗與兩種帶法（講義）。
- 檢核之後的四步範本（原話 → 決定 → 理由 → 下一步）與修正紀錄表。

## 課堂練習

**把 Wireframe 補成能被檢核的一份**（85 分鐘，個人＋跨組配對，Figma）

開始前先挑一條流程：用自己專題的流程，或用三個指定題目其中一題（會員註冊與登入／結帳付款出錯／中途離開與返回）。題目之間沒有分數差別。

1. 狀態盤點（15 分）— 用五欄檢查表逐頁盤，把 Flowchart 攤在旁邊對，至少標出 3 個「缺」。
2. 補畫三種狀態（25 分）— 空狀態 10 分、錯誤狀態 10 分、載入狀態 5 分，每張畫完逐條過檢查清單。
3. 接成 Wireflow 並標註（20 分）— 接線 12 分、標註 8 分。箭頭從可點元件出發，課堂上每張畫面先寫 1 條關鍵標註，回家補到 3 條。
4. 兩人互相檢核（25 分）— 各 10 分鐘互換，最後 5 分鐘各自整理修正清單。要跟不同專題的人配對。

之後另有 15 分鐘成果分享與作業說明（抽點 3–4 位，講被問倒的那一題與打算怎麼改）。

產出：3 張新狀態畫面 + 1 張接起來的 Wireflow + 標註 + 修正清單至少 5 則。

### 三小時時間分配

| 段落 | 時間 | 內容 |
| :--- | :--- | :--- |
| Part 1 | 45 分 | 三種狀態、空狀態三準則、錯誤訊息五要件、表單十條、回應時間與進度指示、三種溝通方式 |
| 休息 | 10 分 | |
| Part 2 | 25 分 | Wireflow 合成、標註、設計說明、設計檢核的規則與回饋改寫 |
| Part 3 | 85 分 | 課堂練習四階段 |
| Part 4 | 15 分 | 成果分享與作業說明 |

講述 70 分 + 實作與分享 100 分 + 休息 10 分 = 180 分。

## 回家作業

**作業 5（下半）：完整 Wireflow、狀態補齊與修正紀錄**

1. 核心畫面補到 3–5 張（狀態版本不另計數），整組畫面裡空狀態、錯誤狀態、載入狀態至少各出現一次。
2. 接成一張完整的 Wireflow，Flowchart 上每一條例外路徑都要找得到對應畫面，不能有斷掉的箭頭。
3. 每張畫面至少 3 條標註，整份至少一條「刻意不做的事」。
4. 修正紀錄至少 5 則，每則四欄（原話、決定、理由、下一步）填滿，決定「不改」的也要寫。
5. 一段設計說明，挑三個版面決策各寫一句「因為研究裡的 ______，所以 ______」。
6. （加分，非必要）把其中一條流程做成 Figma 可點原型。

配分：流程完整性 25、狀態設計 25、標註品質 20、修正紀錄 20、設計說明 10，各項的「通過的樣子」與「不及格的樣子」寫在 `exercises.html#submit`。

交件規格對齊課綱作業 5：**1 張 Flow + 3–5 個 Wireframe**。

## 對應資展日期與時段

- 2026/08/06（四）上午 09:00–12:00
- 資展時程主題：【實務】介面設計流程（下）：介面設計流程延伸與實作

## 本單元產出

- 對應 `資展課程大綱.md` 第五節階段作業表：
- 作業 5：Flowchart + UI Flow + Wireframe，與 Unit 06 共同完成；Unit 06 產出 Flow 與初版 Wireframe，本單元完成狀態補齊、Wireflow 合成與檢核修正。

## 參考資料

- [Designing Empty States in Complex Applications: 3 Guidelines](https://www.nngroup.com/articles/empty-state-interface-design/) — NN/g，空狀態三條準則。
- [Error-Message Guidelines](https://www.nngroup.com/articles/error-message-guidelines/) — NN/g，錯誤訊息五要件。
- [10 Design Guidelines for Reporting Errors in Forms](https://www.nngroup.com/articles/errors-forms-design-guidelines/) — NN/g，表單錯誤回報十條。
- [Response Times: The 3 Important Limits](https://www.nngroup.com/articles/response-times-3-important-limits/) — NN/g，0.1／1／10 秒三門檻。
- [Progress Indicators Make a Slow System Less Insufferable](https://www.nngroup.com/articles/progress-indicators/) — NN/g，進度指示三型別。
- [Indicators, Validations, and Notifications](https://www.nngroup.com/articles/indicators-validations-notifications/) — NN/g，三種溝通方式的分工。
- [Wireflows: A UX Deliverable for Workflows and Apps](https://www.nngroup.com/articles/wireflows/) — NN/g，Wireflow 定義與實作準則。
- [Design Critiques: Encourage a Positive Culture to Improve Products](https://www.nngroup.com/articles/design-critiques/) — NN/g，角色、三個前提與回饋改寫。
- [Closing the Loop: What to Do After a Design Critique Ends](https://www.nngroup.com/articles/after-design-critique/) — NN/g，檢核之後的四步範本。

## 備註

- 原 `slides.html`（介面視覺基礎：版面、排版、色彩與一致性，5 張佔位內容）是舊版課綱的主題，已於本次重製時整份取代。該主題現由 Unit 08「風格發想與建立」涵蓋。
