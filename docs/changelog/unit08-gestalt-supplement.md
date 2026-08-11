# [LOG] Unit 08 補充簡報：增加設計的好感度

對應規格：[docs/spec/unit08-gestalt-supplement.md](../spec/unit08-gestalt-supplement.md)

---

## 2026-08-11 — 完形與 Laws of UX 獨立成補充簡報並修正張數 bug

**修改檔案：**
- `Unit_08/gestalt-lawsofux.html` — 22 張補充簡報（新增）
- `Unit_08/resources/Laws of UX 使用者體驗介面定律.md`、`如何增加介面設計的友善度.md` — 來源（新增）
- `Unit_08/README.md` — 相關檔案清單
- `index.html` — Unit 08 卡片第三個入口

**實作說明：**

內容整份取自舊版 `Unit_09/slides.html`，只改身分標記：`unit-pill` 由「Unit 09」改為「Unit 08」，`course-label` 由「UI 設計實作：Figma 與 UX 流程 × AI 設計整合」改為「風格發想與建立 · 完形心理學與 Laws of UX」，標題與封面主標改為「增加設計的好感度」。

兩份來源 md 從 Unit_09 複製進 `Unit_08/resources/`，Unit_09 原檔保持不動（當時的決定是兩份並存）。

**修正原檔就有的兩個問題：**

- 封面 `cover-meta` 寫「21 張投影片」，實際是 22 張；`slide-num` 的分母也全部寫成 `/21`，只有最後兩張寫 `/22`。一併對齊成 22。
- `#ctrls` 沒有深色頁的樣式，翻頁箭頭在 10 張深色投影片上幾乎看不見。比照其他單元加上 `#ctrls.on-dark button` 規則與 JS 切換。

**已知問題 / 備註：**

這份簡報與 `Unit_09/usability-heuristics.html`（十大易用性延伸教材）內容不同，兩者並存不衝突。
