# Unit 07 來源整理：Wireframe 實作延伸

> 本檔為教材的溯源依據。內容整理自下列來源，查證日期 2026-08-05。
> 教材裡的每個觀念都應該能對回這一份的某一段。

Unit 06 的來源整理（Wireflow 定義、保真度三維度、Auto Layout）在 `../Unit_06/resources/guide.md`，本單元的 Wireflow 段落沿用該檔第 1 節，不重複抄錄。

---

## 1. 空狀態（Empty States）

來源：[Designing Empty States in Complex Applications: 3 Guidelines](https://www.nngroup.com/articles/empty-state-interface-design/) — NN/g，2021-09

空狀態指的是容器、畫面或面板**還沒有內容、或無法顯示內容**時的樣子。最常出現在剛註冊完的 onboarding 階段，以及篩選條件沒有命中任何資料的時候。

NN/g 的核心主張：**不要留全空白**（"Do not default to totally empty states"）。全空白會讓使用者分不清是還在載入、是出錯了、還是真的沒資料。

### 三條準則

**① 傳達系統狀態（Communicate System Status）**

流程跑完之後如果沒有資料可顯示，就用這塊空間放一句系統訊息。

> "A brief system message within the content area at completion of the process (e.g., 'There are no records to display for the selected date range') would be a simple yet effective way to increase the visibility of system status and, therefore, user confidence in the results."

範例：log 詳細面板顯示「There are no records to display for the selected date range」，而不是留白。

**② 提供學習線索（Provide Learning Cues）**

空狀態可以用來教使用者這個功能怎麼用，比冗長的 onboarding 導覽有效，因為它是在使用者真的碰到那個 UI 元件時才出現的。

> These help messages are "pull revelations because they show up only when the user interacts with the corresponding UI element and they are not 'pushed' in any obtrusive or interruptive way."

範例：DataDog 顯示「Star your favorites to list them here」；Power BI 說明內容如何進到「最近瀏覽」區。

**③ 給關鍵任務一條直達路徑（Provide Direct Pathways for Key Tasks）**

空狀態裡要放可以直接點的動作。

> Provide "brief yet explicit instructions or, better yet, link directly to the steps that need to be taken to complete tasks."

範例：警示面板同時放「Create」按鈕與「Learn more」文件連結；Loggly 提供「新增 log 來源」與「用示範資料先逛逛」兩個選項。

### 對照課程

Unit 06 的六種例外路徑裡，「沒資料」與「找不到」兩種對應到這裡。Unit 06 只要求「有畫到這個節點」，Unit 07 要求把節點畫成真的畫面，並且滿足上面三條。

---

## 2. 錯誤狀態與表單錯誤回報

來源：
- [10 Design Guidelines for Reporting Errors in Forms](https://www.nngroup.com/articles/errors-forms-design-guidelines/) — NN/g
- [Error-Message Guidelines](https://www.nngroup.com/articles/error-message-guidelines/) — NN/g

### 錯誤訊息的基本要求

NN/g 對錯誤訊息的定義：

> "A system-generated interruption to the user's workflow that informs the user of an incomplete, incompatible, or undesirable situation."

好的錯誤訊息要「explicit, human-readable, polite, precise, and give constructive advice」——明確、看得懂、有禮貌、精準、給得出下一步。

其他要點：

- 位置靠近出錯的地方，降低記憶負擔。
- 樣式用「bold, high-contrast, and red」，並搭配圖示。
- 區分嚴重程度：警告 vs. 真的擋住流程。
- 語言用白話，避免技術術語。
- 「Concisely and precisely describe the issue」——不要只丟一句籠統的話。
- 保留使用者已經填的內容，讓他修改而不是重來。
- 主動偵測常見失誤（例如信件說「附件」卻沒有附檔）。
- 錯不是使用者的問題：「When users make errors, it's not their fault. Errors highlight flaws in your design.」

### 表單錯誤回報十條準則

要做的（1–5）：

| # | 準則 | 重點 |
| :--- | :--- | :--- |
| 1 | 盡量用 inline 驗證 | 「as soon as the user has finished filling in a field, an indicator should appear nearby if the field contains an error」 |
| 2 | 複雜欄位要給成功回饋 | 密碼強度這類難填的欄位，填對了也要說 |
| 3 | 錯誤訊息貼著欄位放 | 訊息與欄位同時看得到，使用者不用記著訊息再回去改 |
| 4 | 用顏色區分狀態 | 紅＝錯誤，橘／黃＝警告，綠／藍＝成功 |
| 5 | 加圖示或輕微動態 | 「An icon to the left of your error message or validation summary will draw attention to the error and help users who are colorblind」 |

不要做的（6–10）：

| # | 準則 | 重點 |
| :--- | :--- | :--- |
| 6 | 少用 modal 與確認對話框 | 打斷流程，而且使用者得記住指示才能回去改 |
| 7 | 不要在使用者填完之前就驗證 | 打到一半跳紅字，很煩 |
| 8 | 不要只給彙總訊息 | 只放頁首的「有 3 個欄位有誤」會「force the user to search for the field in error」 |
| 9 | 不要用 tooltip 報錯 | 「Alert icons are hard to notice, especially on visually dense interfaces」，而且要 hover 才看得到 |
| 10 | 重複出錯要給額外協助 | 同一個錯誤出現三次以上，去查根因，那是設計的問題 |

### 對照課程

Unit 06 的例外路徑「出錯」與「沒權限」對應到這裡。學生在 Wireframe 上最常見的做法是畫一個紅色 modal 說「錯誤」——第 6、9 條就是在講這件事。

---

## 3. 載入狀態與回應時間

來源：
- [Response Times: The 3 Important Limits](https://www.nngroup.com/articles/response-times-3-important-limits/) — NN/g（原始出處為 Nielsen 1993 *Usability Engineering*）
- [Progress Indicators Make a Slow System Less Insufferable](https://www.nngroup.com/articles/progress-indicators/) — NN/g

### 三個門檻

| 時間 | 使用者的感受 | 介面該給什麼 |
| :--- | :--- | :--- |
| 0.1 秒 | 「about the limit for having the user feel that the system is reacting instantaneously」 | 不用特別回饋，直接出結果 |
| 1.0 秒 | 「about the limit for the user's flow of thought to stay uninterrupted」 | 不用特別回饋，但使用者會察覺到延遲 |
| 10 秒 | 「about the limit for keeping the user's attention focused on the dialogue」 | 要有進度指示，而且要能中斷 |

超過 10 秒：「users will want to perform other tasks while waiting for the computer to finish, so they should be given feedback indicating when the computer expects to be done.」

### 進度指示的三種型別

| 型別 | 用在多長的等待 | 說明 |
| :--- | :--- | :--- |
| 循環動畫（spinner） | 2–10 秒 | 「This indicator should be reserved for actions that take between 2-10 seconds.」不到 1 秒就別放，會變干擾；超過 10 秒也不夠，使用者覺得沒在前進就會失去耐性 |
| 百分比進度條 | 10 秒以上 | 「Percent-done progress indicators should be used for longer processes that take 10 or more seconds.」速度變化使用者會察覺並影響滿意度，所以速度要穩定，或先慢後快 |
| 靜態文字（Loading…） | 不建議 | 「static indicators should be replaced with another type of indicator, because they do not offer enough information」 |

研究數據：看得到動態進度回饋的人「experienced higher satisfaction and were willing to wait on average 3 times longer」。

---

## 4. 指示器、驗證、通知的分工

來源：[Indicators, Validations, and Notifications: Pick the Correct Communication Option](https://www.nngroup.com/articles/indicators-validations-notifications/) — NN/g

| | 指示器 Indicator | 驗證 Validation | 通知 Notification |
| :--- | :--- | :--- | :--- |
| 定義 | 標示動態內容或 UI 元件的視覺提示，「contextual」且「conditional—they are not always present, but appear or change depending on certain conditions」 | 針對使用者輸入的回應，說明剛剛輸入的資料是否不完整或不正確 | 「alert the user of general occurrences within a system」，不一定和當下的動作有關 |
| 觸發者 | 內容變動 | 使用者輸入 | 系統事件 |
| 需要使用者動作 | 否 | 是 | 看類型 |
| 範圍 | 針對某個元件 | 針對某個輸入 | 可能是局部，也可能是全域 |
| 常見做法 | 圖示、粗體、顏色、大小、動態 | 貼著欄位的錯誤訊息 | 徽章數字、橫幅、彈窗 |

通知再分兩類：

- **需要動作的通知**：「often urgent and should be intrusive; for instance, they could be implemented as modal popups」。
- **被動通知**：「not urgent and should be less intrusive. A typical implementation of a passive notification may be a badge icon」。

用錯的代價：把該當指示器的資訊做成通知，使用者會直接忽略還覺得煩；把錯誤訊息做成一閃即逝的 toast，使用者根本沒看到——NN/g 提到有位行動裝置受測者「spent 5 minutes waiting for some content to load only because she hadn't notice the little error message」。

---

## 5. 設計檢核（Design Critique）

來源：
- [Design Critiques: Encourage a Positive Culture to Improve Products](https://www.nngroup.com/articles/design-critiques/) — NN/g
- [Closing the Loop: What to Do After a Design Critique Ends](https://www.nngroup.com/articles/after-design-critique/) — NN/g

### 定義

Design critique 是分析一份設計、判斷它有沒有達成它自己的目標。「A design critique usually manifests as a group conversation with the ultimate goal of improving a design.」

要跟 **design review** 分開：critique 只為了改善這份作品；review 是依據 heuristic 做評估，常常帶有核可的性質。

### 角色

| 角色 | 做什麼 |
| :--- | :--- |
| 提案者 Presenter | 呈現設計 |
| 評論者 Critiquer | 給出有依據的回饋與觀點 |
| 引導者 Facilitator | 管控討論、界定範圍、提問、記錄 |
| 記錄者 Recorder | 公開做筆記（有時由 facilitator 兼任） |
| 參與者 Participants | 跨職能的成員 |

### 三個前提

1. **清楚的範圍。** 沒有明確界線的 critique 會失控。
2. **講好的設計目標。** 「In order to analyze a design and whether it meets its goals, there must be agreement on the problem that needs to be solved.」要先對 persona、痛點、使用者任務有共識。
3. **是對話不是命令。** 用指令的方式講話，會扼殺 critique 需要的開放討論。

### 引導者要做的

- 事前發出範圍與議程。
- 讓參與者知道哪些該談、哪些不該談。
- 訂好規則與期待。
- 事先把作品發出去，避免現場的反射式回饋。
- 確認大家對 persona、痛點、使用者任務有共識。

### 提案者要做的

- 先重述目標、摘要 persona，再開始收回饋。
- 講作品的來龍去脈，然後**具體說明你要哪一種回饋**。
- 講快一點，不要一直替設計決策辯解。
- 不要把回饋當成人身攻擊。

### 評論者要做的

把意見轉成對著目標問的問題，不要講個人偏好。

| 不好的回饋 | 改寫 |
| :--- | :--- |
| 「That button is in the wrong spot.」 | 「If the goal is quick registration, placing the button here may emphasize the wrong elements.」 |
| 「Yikes… that layout!」 | 「How does this layout make it easier for the user to accomplish their task quickly and efficiently?」 |

### 兩種引導方式

- **Round robin**：每個人輪流講，確保都有出聲。
- **Quotas**：引導者要求每人講固定數量的正面與負面意見，用來破冰。

### 常見的失敗

- 事前沒有對 persona 或目標達成共識。
- 場次排太長。
- 把回饋當成針對個人。
- 急著在 critique 現場就把問題解決掉。
- 只講缺點。

### 結束之後：close the loop

Critique 不是散會就結束。三個該回頭交代的時機：

1. 設計有重大改動之後——把改動前後的截圖發出去，並註明是誰的意見促成的。
2. 交給開發之前——讓相關人在 demo 或上線前就知道最終決定。
3. 回饋影響了大方向的時候——把當初的意見與後來的決策明確接起來。

處理單則回饋的四步範本：**點名那則回饋 → 說出你的決定 → 說明理由 → 說接下來會怎樣。** 不論那則回饋是「有道理但這次不做」還是「被可用性測試的數據推翻」，都用同一套。

兩種收尾：

- **即時摘要**：一則短訊息，寫「我們要往前做的是什麼、還在查的是什麼、決定不做的是什麼」。
- **後續文件**：把改動接回當時的對話。「This changed because you said that closes the loop.」

核心：「Critique followups make feedback feel worth giving rather than a nice-to-have or a courtesy.」

---

## 6. 課程對照表

| 教材段落 | 來源 |
| :--- | :--- |
| 一個畫面不只一個樣子 | 第 1、2、3 節綜合 |
| 空狀態三條準則 | 第 1 節 |
| 錯誤訊息與表單十條 | 第 2 節 |
| 0.1／1／10 秒與進度指示 | 第 3 節 |
| Indicator／Validation／Notification | 第 4 節 |
| Wireflow 合成 | Unit 06 guide 第 1 節 |
| 設計說明與同儕檢核 | 第 5 節 |
