# 練習：會員登入頁面 (Member Login) Wireframe 設計

這是一個針對「單元 2：Figma 基礎操作」所設計的會員登入頁面 Wireframe 結構。

## 1. 頁面結構 (Layout Structure)

### Header (頁首)
- **左側**：品牌 Logo (Placeholder)
- **右側**：語系切換 (Language Switcher) 或 關閉按鈕 (X)

### Main Content (核心內容區) - 置中對齊
- **標題 (H1)**: 歡迎回來 (Welcome Back)
- **副標題 (Body)**: 請輸入您的帳號密碼以繼續。
- **第三方登入區 (Social Auth)**:
  - [G] 使用 Google 帳號登入 (Button)
  - [f] 使用 Facebook 帳號登入 (Button)
- **分隔線**: 或是 (OR)
- **表單區 (Form)**:
  - **Label**: 電子郵件 / 帳號
    - [ Input Field: 請輸入 Email ]
  - **Label**: 密碼
    - [ Input Field: 請輸入密碼 ] (右側含「顯示/隱藏密碼」圖示)
  - **輔助連結**: [ 忘記密碼？ ] (靠右對齊)
- **主按鈕 (Primary Button)**: 立即登入 (Login)
- **註冊提示**: 還沒有帳號嗎？ [ 立即註冊 ]

### Footer (頁尾)
- **連結**: 隱私權政策 | 服務條款
- **版權**: © 2026 UI/UX Class. All rights reserved.

---

## 2. AI 輔助設計建議 (AI UX Hints)

1.  **文案優化**：
    - 不要只寫 "Login"，改用 "Welcome Back!" 增加親和力。
    - 錯誤訊息示範：如果密碼錯了，不要只說「錯誤」，改用「密碼不正確，請再試一次，或點擊忘記密碼」。
2.  **可用性原則 (Usability)**：
    - **Fitts's Law**：登入按鈕應足夠大，方便點擊（高度建議 44px - 56px）。
    - **錯誤預防**：在使用者還沒輸入內容前，將「登入」按鈕設為 Disabled (灰階)。
3.  **Figma 實作技巧 (For Unit 02)**：
    - 使用 **Auto Layout** 處理 Input Field 與 Label 的垂直間距 (建議 8px)。
    - 使用 **Components** 製作登入按鈕，方便後續切換 Hover/Disabled 狀態。

---

## 3. Wireframe 視覺示意 (ASCII)

```text
+------------------------------------------+
|  [Logo]                          [EN] [X]|
+------------------------------------------+
|                                          |
|              Welcome Back!               |
|         Please enter your details        |
|                                          |
|        [ G Log in with Google    ]       |
|        [ f Log in with Facebook  ]       |
|                                          |
|              ---- OR ----                |
|                                          |
|   Email                                  |
|   [ bryan@example.com            ]       |
|                                          |
|   Password                               |
|   [ ************             (o) ]       |
|                          Forgot? [?]     |
|                                          |
|        [[      LOG IN      ]]            |
|                                          |
|        Don't have an account? Sign up    |
|                                          |
+------------------------------------------+
|      Privacy Policy  |  Terms of Use     |
+------------------------------------------+
```
