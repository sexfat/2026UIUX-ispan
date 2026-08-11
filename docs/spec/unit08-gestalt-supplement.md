# [SPEC] Unit 08 補充簡報：增加設計的好感度

- **日期**：2026-08-11
- **負責人**：bryant_huang
- **狀態**：done
- **變更紀錄**：[docs/changelog/unit08-gestalt-supplement.md](../changelog/unit08-gestalt-supplement.md)

---

## 背景

Unit 08「風格發想與建立」的主簡報中，完形心理學與 Laws of UX 只保留成風格板的檢查表，且被標記為 `drop` 的備用補充頁，預設不播——因為 180 分鐘的課堂時間要留給風格板實作，不展開成理論課。

但這兩組內容的完整版（完形 8 大原則、Laws of UX 7 條定律）有獨立的教學價值，舊版 Unit_09 就有一份完整簡報。Unit 09 改為 RWD 主題後，這份內容需要一個不佔課堂時間的去處。

## 功能說明

一份 22 張的獨立補充簡報，與 Unit 08 主簡報並存，供課後自學或延伸參考：

1. **完形心理學 8 大原則**——接近性、相似性、封閉性、連續性、圖形與背景、共通命運、簡單性、突出性，每條配真實介面案例圖。
2. **Laws of UX 7 條定律**——Hick's Law、Doherty Threshold、Fitts's Law、美即是好效應、目標漸近效應、Jakob's Law、Miller's Law。
3. **學習檢核表**——兩組各 7 項，可點擊勾選。

## 實作範圍

- `Unit_08/gestalt-lawsofux.html`：22 張補充簡報，內容取自舊版 Unit_09，單元標記改為 Unit 08。
- `Unit_08/resources/`：完形心理學、Laws of UX 兩份來源 md，建立溯源依據。
- `Unit_08/README.md`：相關檔案清單補上這份簡報。
- `index.html`：Unit 08 卡片新增第三個入口。

## 不在範圍內

- 不調整 Unit 08 主簡報中完形與 Laws of UX 的既有處理方式（仍維持 `drop` 備用頁）。
- 不重新撰寫內容，沿用舊版 Unit_09 的既有教材。

## 驗收條件

- [x] 22 張投影片，封面標示與實際張數一致（修正原檔 21/22 不符的 bug）
- [x] `slide-num` 分母全部對齊為 22
- [x] 翻頁箭頭在深色頁有 `on-dark` 反白
- [x] 首頁 Unit 08 卡片可進入
