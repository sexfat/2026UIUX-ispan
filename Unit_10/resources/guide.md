# Unit 10 來源整理：Mockup 精度與十大易用性

> 本檔為教材的溯源依據。查證日期 2026-08-09。
> 教材裡的每個觀念都應該能對回這一份的某一段。

主要來源：[使用者介面設計的10大易用性](https://www.71next.com/userDoc/10-usability-heuristics/) — 71NEXT 使用者體驗設計 UXI。該文的原始依據是 NN/g 的 [10 Usability Heuristics for User Interface Design](https://www.nngroup.com/articles/ten-usability-heuristics/)。

十大原則的**順序、中文標題與 Tips 全部照 71next 原文**，本檔逐條抄錄原句，教材不自行增刪原則。

風格板、色彩、字級、完形與 Laws of UX 的來源整理在 `../Unit_08/resources/`，本單元不重複整理，需要時指回去。

---

## 圖片對照表

16 張圖全部下載在 `heuristics/`，來源是 71next 該篇文章內嵌的圖片（71next 本身多數為外部連結）。**課堂教學引用，正式作品集不可沿用。**

| 檔名 | 原始網址 | 內容 | 71next 放在哪一條 |
| :--- | :--- | :--- | :--- |
| `h01-visibility-loading.gif` | behance.net | 底部分頁列切換動畫，目前所在分頁會亮起並顯示標籤 | #1 |
| `h01-visibility-progress.jpg` | pinimg.com | 九種進度指示器樣式（進度條、百分比、步驟條、環形、圓點） | #1 |
| `h02-real-world-icons.jpg` | 71next 自存 | cPanel 檔案管理員工具列：每個功能都是「圖示＋中文字」 | #2 |
| `h03-user-control.jpg` | pinimg.com | iOS 的 BBC News 通知設定頁，使用者自己決定要不要收通知、收哪幾種 | #3 |
| `h04-consistency-styleguide.jpg` | dribbble.com | AfterShip 的 StyleGuide：字體、色票、按鈕、表單、圖示一次定義 | #4 |
| `h05-error-prevention-confirm.png` | pinimg.com | Twitter 註冊表單的即時驗證，電話與密碼欄位當場標紅並說明原因 | #5 |
| `h05-error-prevention-github.png` | 71next 自存 | GitHub 刪除 repo 的 Danger Zone 與二次確認對話框 | #5 |
| `h06-recognition-netflix.jpg` | 71next 自存 | Netflix「繼續觀賞」列，每張縮圖下方有紅色觀看進度條 | #6 |
| `h06-recognition-folders.png` | medium.com | 左邊 Terminal 打指令（✗）對比右邊 Finder 圖像化資料夾（✓） | #6 |
| `h07-flexibility-nike.jpg` | 71next 自存 | Nike 男鞋列表頁的左側篩選（性別、價格、促銷、尺寸） | #7 |
| `h07-flexibility-shortcuts.png` | medium.com | Google 圖片搜尋的 Search tools 進階篩選（Size／Color／Type／Time） | #7 |
| `h08-minimalist.png` | medium.com | Google 首頁：一個搜尋框、兩顆按鈕，其他全部拿掉 | #8 |
| `h09-error-404.jpg` | freepik.com | 404 頁面版型，插圖＋「Oops!, Page not Found」＋ Go back home 按鈕 | #9（教材另借用於 #3，見下方說明） |
| `h09-error-feedback.gif` | dribbble.com | 「Oh no! Something went wrong, we're digging for a solution.」＋ Go home | #9 |
| `h10-help-docs-a.png` | medium.com | ✗ 反例：「Error / The operation couldn't be completed. (ErrorDomain error 20.)」 | #10（見下方說明） |
| `h10-help-docs-b.png` | medium.com | ✓ 正例：「Uh oh! The file you tried to upload is a type we don't understand. Supported image formats are JPEG, PNG, and GIF.」 | #10（見下方說明） |

**檔名與 71next 版面位置的落差（重要）：** 最後兩張在 71next 原文是掛在 #10「教學指示與幫助」下面，所以檔名前綴保留 `h10-`。但它們的內容是**錯誤訊息寫法的正反例**（有錯誤代碼 vs 白話說明＋支援格式），對應的是 #9 的「錯誤訊息應該用簡單的語言（沒有錯誤代碼）表達」。教材把這兩張用在 #9，不是照原文放在 #10——這是刻意的調整，因為放在 #10 會讓學生誤以為那是說明文件的例子。

**`h09-error-404.jpg` 的跨條目借用：** 這張在原文屬於 #9，教材把它放在簡報 #3「控制權與自由度」那一頁，用來說明「死路也要有出口」。投影片的 figcaption 已標明它原本屬於第 9 條，避免學生誤記對應關係。同一張畫面同時被好幾條原則管到，本來就是常態。

---

## 十大易用性原則（逐條抄錄 71next 原文）

### #1 系統狀態的可見性（Visibility of System Status）

> 設計應始終透過在合理的時間內提供適當的回饋，讓使用者了解正在發生的事情。
>
> 當使用者知道當前的系統狀態時，他們會了解先前互動的結果並確定後續步驟。可預測的互動可以建立對產品和品牌的信任。

**Tips：** 向使用者清楚傳達系統的狀態

圖：`h01-visibility-loading.gif`、`h01-visibility-progress.jpg`

---

### #2 連結真實世界（Match between system and the real world）

> 設計應該遵守使用者的語言。使用使用者熟悉的單字、短語和概念，而不是內部術語。
>
> 遵循現實世界的慣例，使資訊以自然且符合邏輯的順序出現。

**Tips：** 善用 icon 來表示功能

圖：`h02-real-world-icons.jpg`

---

### #3 讓使用者有控制權及自由度（User control and freedom）

> 使用者經常會錯誤地執行操作。他們需要一個明確標記的「回到上一頁或是跳出服務」來離開不需要的行動，而不必經歷漫長的過程。
>
> 允許使用者對系統的控制，避免陷入困境和感到沮喪。

**原文舉的例子：**
1. Airbnb 在挑選房間時，可以透過切換地圖模式或列表模式來瀏覽房型，提供兩種不同的篩選方式來找尋理想的房型。
2. 選機票或是飯店時，可以挑選不同的日期跟航班（booking.com）

圖：`h03-user-control.jpg`

---

### #4 一致性與標準（Consistency and Standards）

> 人們大部分時間都花在使用您的產品之外的數位產品上。
>
> 使用者對其他產品的體驗決定了他們的期望。未能保持一致性可能會迫使使用者學習新東西，從而增加使用者的認知負擔。

**Tips：** 確保設計中使用元素和操作方式相同。Design Guideline。

圖：`h04-consistency-styleguide.jpg`

---

### #5 預防錯誤（Error Prevention）

> 良好的錯誤訊息很重要，但最好的設計首先會仔細防止問題的發生。消除容易出錯的情況，要么檢查它們並在用戶承諾操作之前向用戶提供確認選項。
>
> 錯誤有兩種類型：一種是失誤，一種是錯誤。
>
> 失誤是由於注意力不集中而導致的無意識錯誤。錯誤是基於使用者心理模型與設計之間不匹配的有意識的錯誤。

**Tips：**
1. 先防止高成本的錯誤
2. 設定預設值來防止錯誤
3. 警告用戶來防止重大錯誤的產生

圖：`h05-error-prevention-confirm.png`、`h05-error-prevention-github.png`

> 名詞對照（NN/g 原文用詞）：失誤 = slip，錯誤 = mistake。

---

### #6 用認知方式而非記憶（Recognition rather than recall）

> 透過使元素、操作和選項可見來最小化使用者的記憶體負載。
>
> 使用者是認知不是記憶住元素，增加認知的介面減少了使用者所需的認知負荷。

**Tips：**
1. 讓人們識別介面中的信息，而不是強迫他們記住
2. 減少用戶必須記住的資訊。

**原文舉的例子：**
- Netflix 開啟時，每個影片或影集看過的時間進度都會自動紀錄，因此使用者無需記得上次看到第幾集，能夠更省力得繼續看下去。
- 使用資料夾的圖象化，方便我們找資料
- 購物車

圖：`h06-recognition-netflix.jpg`、`h06-recognition-folders.png`

---

### #7 具備使用靈活性和效率（Flexibility and efficiency of use）

> 靈活的流程可以透過不同的方式進行，以便人們可以選擇適合自己的方法。

**Tips：**
1. 提供鍵盤快速鍵和觸控手勢等加速器。
2. 透過為個人用戶客製化內容和功能來提供個人化。
3. 允許定制，因此用戶可以選擇他們希望產品如何運作。

圖：`h07-flexibility-nike.jpg`、`h07-flexibility-shortcuts.png`

---

### #8 設計美觀與極簡（Aesthetic and Minimalist Design）

> 避免提供不必要的元素和信息，以免分散使用者注意力。確保介面的視覺元素只能關注使用者的主要目標。

**Tips：**
1. 讓 UI 的內容和視覺設計集中在重點上。
2. 不要讓不必要的元素分散使用者對他們真正需要的資訊的注意力。
3. 優先考慮支援主要目標的內容和功能。

圖：`h08-minimalist.png`

---

### #9 易於使用的錯誤處理和回饋（User-friendly Error Handling and Feedback）

> 錯誤訊息應該用簡單的語言（沒有錯誤代碼）表達，準確地指出問題，並建設性地提出解決方案。

**Tips：**
1. 使用傳統的錯誤訊息視覺效果，例如粗體、紅色文字。
2. 用他們能理解的語言告訴使用者出了什麼問題—避免使用技術術語。
3. 為用戶提供一個解決方案，就像一個可以立即解決錯誤的捷徑。

圖：`h09-error-404.jpg`、`h09-error-feedback.gif`，另加 `h10-help-docs-a.png`／`h10-help-docs-b.png`（正反例，見上方圖片對照表的說明）

> 對照 NN/g 原文，這一條的英文標題是 "Help users recognize, diagnose, and recover from errors"。71next 譯為「易於使用的錯誤處理和回饋」，教材沿用 71next 的中文標題。

---

### #10 教學指示與幫助（Help and Documentation）

> 介面提供簡易教學，讓新的使用者迅速上手使用。
>
> 最好係統不需要任何額外的解釋。但是，可能有必要提供文件來幫助使用者了解如何完成其任務。

**Tips：**
1. 確保幫助文件易於搜尋。
2. 只要有可能，就在使用者需要時在上下文中呈現文件。
3. 列出要執行的具體步驟。

---

## 71next 該篇列出的參考文章

- https://www.nngroup.com/articles/ten-usability-heuristics/
- https://www.nngroup.com/articles/usability-heuristics-virtual-reality/
- https://uxdesign.cc/10-usability-heuristics-every-designer-should-know-129b9779ac53
- NN/g 十大易用性海報下載

---

## 來源 → 課程哪一段用到

| 來源段落 | 用在哪 |
| :--- | :--- |
| #1 系統狀態的可見性 | 簡報 Part 2 第一條；講義第 6 節；練習階段二檢查表第 1 條 |
| #2 連結真實世界 | 簡報 Part 2；講義第 6 節；練習檢查表第 2 條 |
| #3 控制權與自由度 | 簡報 Part 2；講義第 6 節；練習檢查表第 3 條 |
| #4 一致性與標準 | 簡報 Part 2；講義第 7 節（接回 Unit 08 風格板） |
| #5 預防錯誤（失誤 vs 錯誤） | 簡報 Part 2；講義第 7 節；練習階段三的錯誤預防改稿 |
| #6 認知而非記憶 | 簡報 Part 2；講義第 7 節 |
| #7 靈活性與效率 | 簡報 Part 2；講義第 8 節 |
| #8 美觀與極簡 | 簡報 Part 2；講義第 8 節 |
| #9 錯誤處理與回饋 | 簡報 Part 2；講義第 8 節；練習階段三改錯誤訊息 |
| #10 教學指示與幫助 | 簡報 Part 2；講義第 8 節 |
| 圖片對照表 | 簡報 Part 2 每一條的配圖、講義第 6–8 節的 `.fig` |

Mockup 精度（間距、狀態、真實內容）與 Figma 元件落地的段落，依據來自 `../Unit_08/resources/` 的風格板與設計系統整理，以及 Unit 08 講義第 11 節「從風格板長成設計系統」，本檔不重複抄錄。
