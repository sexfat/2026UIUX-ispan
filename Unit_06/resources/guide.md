# Unit 06 來源整理：Flowchart 到 Wireframe

> 本檔為教材的溯源依據。內容整理自下列來源，查證日期 2026-08-01。
> 教材裡的每個觀念都應該能對回這一份的某一段。

---

## 1. 四種流程圖：Flowchart／User Flow／Wireflow／User Journey

來源：
- [Wireflows: A UX Deliverable for Workflows and Apps](https://www.nngroup.com/articles/wireflows/) — NN/g
- [User Journeys vs. User Flows](https://www.nngroup.com/articles/user-journeys-vs-user-flows/) — NN/g
- [UX Deliverables: Glossary](https://www.nngroup.com/articles/ux-deliverables-glossary/) — NN/g

### User Journey vs. User Flow

NN/g 的定義：

- **User Journey**：「a scenario-based sequence of the steps that a user takes in order to accomplish a high-level goal」——跨通路、跨時間的高層目標。
- **User Flow**：「a set of interactions that describe the typical or ideal set of steps needed to accomplish a common task performed with a product」——單一產品內、完成一個任務的步驟。

| 面向 | User Journey | User Flow |
| :--- | :--- | :--- |
| 尺度 | 宏觀 | 微觀 |
| 時間 | 數天、數週、數月 | 數分鐘到數小時 |
| 通路 | 多個接觸點、跨通路 | 單一產品內 |
| 內容 | 行動、情緒、想法、通路 | 產品互動與系統回應 |
| 產出物 | 旅程地圖 | Wireflow、Flowchart、Task diagram |
| 研究方法 | 田野研究、日記研究、訪談 | 可用性測試、數據分析 |

關係：User Flow 是 User Journey 裡某一段的放大。

> 課程對照：User Journey 是 Unit 04 做過的旅程地圖；Unit 06 做的是 User Flow。

### Flowchart vs. Wireframe vs. Wireflow

- **Flowchart**：能完整記錄複雜的多步驟工作流程，但**缺少畫面脈絡**（lack the page context），而畫面脈絡強烈影響使用者體驗。
- **Wireframe**：擅長表達版面，但**不擅長記錄互動**，尤其對「頁面少、內容靠互動動態變化」的產品（AJAX 型）力有未逮。
- **Wireflow**：「combines wireframe-style page layout designs with a simplified flowchart-like way of representing interactions」。用畫面設計取代抽象流程圖符號，讓焦點留在使用者實際會操作的產品上。

適用時機：

| 產品型態 | 用什麼 |
| :--- | :--- |
| 頁面多、各頁相對靜態的網站 | Wireframe |
| 複雜的多步驟工作流程要窮盡記錄 | Flowchart |
| 頁面少、內容依互動動態變化的 App／Web App | Wireflow |

Wireflow 的實作準則：

- 低保真（草圖、發想用）與高保真（規格用）都可行。
- 每個節點呈現的是**畫面狀態**——整個畫面，或只呈現有變動的區塊。
- 箭頭要指向**具體可點的 UI 元件**（hotspot），並清楚指出結果畫面，包含確認彈窗、顏色變化這類視覺回饋。
- 桌機因為畫面大，建議只畫有變動的介面元素，不要每個節點都畫整頁。

Wireflow 最初是行動 App 團隊的常見作法，每個流程步驟就是一張完整的手機畫面。

---

## 2. 保真度：Low-Fidelity vs. High-Fidelity

來源：[UX Prototypes: Low Fidelity vs. High Fidelity](https://www.nngroup.com/articles/ux-prototype-hi-lo-fidelity/) — NN/g

保真度不是單一刻度，而是**三個獨立的維度**：

| 維度 | 低保真 | 高保真 |
| :--- | :--- | :--- |
| 互動性 Interactivity | 需要人工在旁邊換畫面 | 連結與選單真的能點 |
| 視覺 Visuals | 手繪草圖、灰階方塊 | 完整的層級、間距、版面 |
| 內容 Content | 摘要與佔位符 | 真實的文章與圖片 |

**高保真的優點**

- 系統回應快，不打斷使用者的認知流。
- 能測到特定 UI 元件、工作流程，以及可視線索（affordance）、易讀性這類視覺問題。
- 使用者的行為更接近真實，會把它當成真的軟體在用。
- 設計師可以專心觀察，而不是忙著操作原型。
- 減少人為操作失誤。

**低保真的優點**

- 準備快，省下的時間可以拿去多迭代幾輪。
- 測試中途就能改：現場畫一畫就好。
- 對使用者的壓迫感低，比較不怕「做錯」，也更願意給負面回饋。
- 設計師不會過度投入在還沒驗證的想法上。
- 利害關係人看得出來還沒完成，會預期它還要改。

**選擇原則**：要測真實互動、且資源足夠時用高保真；要快速探索概念、要拿到對概念本身的回饋時用低保真。

> 課程對照：Unit 06 刻意停在低保真，理由就是上面「設計師不會過度投入」與「利害關係人預期它還會改」這兩條。

---

## 3. Figma Auto Layout

來源：[Guide to auto layout](https://help.figma.com/hc/en-us/articles/360040451373-Guide-to-auto-layout) — Figma Help Center

Auto layout 讓 frame 隨內容變動自動反應：元素依**方向、間距、內距、對齊**等屬性自動排列。

### 三種排列方向（flow）

| 方向 | 行為 | 典型用途 |
| :--- | :--- | :--- |
| 垂直 Vertical | 沿 y 軸排列 | 清單項目 |
| 水平 Horizontal | 沿 x 軸排列，可換行（wrap） | 按鈕列 |
| 網格 Grid | 佔用行與列，可跨格 | 儀表板 |

### 間距

- **Padding（內距）**：frame 邊緣與子元件之間的留白。可統一設定，或分別設上下左右。
- **Gap between（間隔）**：子元件之間的距離。可給固定數值，或設為 `Auto` 讓元件平均散開。

### 三種尺寸模式（resizing）

| 模式 | 可套用在 | 行為 |
| :--- | :--- | :--- |
| Hug contents | **只有** auto layout frame | 縮到剛好包住內容 |
| Fill container | **只有**子元件 | 撐滿父容器的可用空間（會遵守間距設定） |
| Fixed | frame 與子元件都可以 | 尺寸固定，不隨周圍變動 |

**關鍵規則**：只要 auto layout frame 裡有任何子元件設成 Fill container，父 frame 在那個軸向就**不再是 Hug，會自動變成 Fixed**。這是學生最常卡住的地方。

另可疊加最小 / 最大尺寸限制。

### Absolute position（忽略 auto layout）

設成絕對定位的物件會跳出排列流程，但仍留在 frame 內，位置相對於父容器精確定位。**這種物件改用 Constraints，而不是 resizing 模式。**

快捷鍵：Mac 按住 `Ctrl` 拖曳／Windows 按住 `S` 拖曳。

### 巢狀

巢狀 auto layout frame 可以組合多種方向做出複雜介面。每一層 frame 各自有獨立的 padding 與 gap。

### 快捷鍵

| 動作 | Mac | Windows |
| :--- | :--- | :--- |
| 加上 auto layout | `⇧ A` | `Shift A` |
| 移除 auto layout | `⌥ ⇧ A` | `Alt Shift A` |
| 設為 Hug contents | 雙擊 frame 邊緣 | 同左 |
| 設為 Fill container | `⌥` + 雙擊 | `Alt` + 雙擊 |
| 對齊 | 方向鍵 `↑ ↓ ← →`；靠邊 `W A S D` | 同左 |

---

## 4. Figma Constraints

來源：[Apply constraints to define how layers resize](https://help.figma.com/hc/en-us/articles/360039957734-Apply-constraints-to-define-how-layers-resize) — Figma Help Center

Constraints 告訴 Figma：**當 frame 被縮放時，圖層要怎麼反應。**

| 水平 | 行為 |
| :--- | :--- |
| Left | 維持與左邊界的距離 |
| Right | 維持與右邊界的距離 |
| Left and Right | 同時固定左右，圖層寬度會跟著伸縮 |
| Center | 對齊 frame 水平中線 |
| Scale | 尺寸與位置依 frame 等比縮放 |

垂直同理：Top／Bottom／Top and Bottom／Center／Scale。

**重要**：Constraints **不能**套用在 auto layout frame 裡的一般子元件——兩套機制是獨立的。auto layout 的子元件用 resizing 模式（Fixed／Hug／Fill）；只有設成 absolute position 的子元件才會回到 constraints。

用途：多裝置的響應式版面、frame 縮放時維持元素位置、控制巢狀 frame 內的行為。

---

## 5. 本單元定位

- 資展時段：2026/08/03（一）13:30–16:30，3 小時。
- 階段作業 5「Flowchart + UI Flow + Wireframe」橫跨 Unit 06–07，交件為 1 張 Flow + 3–5 個 Wireframe。
- Unit 06 產出 Flow 與**初版**低保真 Wireframe；細修與延伸留給 Unit 07。
- 上游輸入：Unit 05 的 IA 圖與功能清單。
