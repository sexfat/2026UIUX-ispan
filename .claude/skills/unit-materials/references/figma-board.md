# Figma / FigJam 練習板

給學生操作的板子要**預先建好素材**。空白連結等於沒做——上課前十分鐘沒有人有空貼 13 張便利貼。

## 前置

1. 呼叫 `use_figma` 前**必須**先載入 figma-use skill（或讀 `skill://figma/figma-use/SKILL.md`）。跳過會踩一堆難查的錯。
2. **Codex 在 headless（`codex exec`）模式下寫不了 Figma**：`use_figma` 需要互動核准，會回 `user cancelled MCP tool call`，連最小測試腳本也一樣。Codex 可以建空檔案，內容要由 Claude Code 這邊補。
3. 帳號底下有多個 team 時，`create_new_file` 會要求先指定。先跑 `whoami` 看哪個是 Full seat，然後**問用戶要建在哪個 team**，不要自己選。

## FigJam 的三個坑

**1. Section 子節點用相對座標。**

`section.appendChild(node)` 之後，`node.x` 是相對於 section 左上角，不是畫布絕對座標。把絕對座標直接設上去，元素會整批飛到隔壁區。

```js
// 錯：section 在 x=1000，這張卡片會跑到絕對座標 2060
sticky.x = 1060;

// 對：相對於 section
sticky.x = 60;
// 驗證：node.absoluteTransform[0][2] 才是絕對 x
```

**2. `TableNode` 沒有 resize。**

`table.resize()` 與 `resizeWithoutConstraints()` 都不存在，會丟 `no such property 'resize' on TABLE node`。表格只能用預設寬度，要在教材裡註明學生可自行拉寬。

**3. 節點型別跟 design mode 不一樣。**

FigJam 可用：`createSticky`、`createSection`、`createShapeWithText`、`createConnector`、`createText`、`createTable`。`figma.createPage()` 在 FigJam 會丟錯。

## 中文字型

`Inter` 沒有中文字符。全部文字用 `Noto Sans TC`（有 Regular／Medium／Bold），**設 characters 前先 `await figma.loadFontAsync()`**。Sticky 的預設字型是 Inter，要先設 `sticky.text.fontName` 再設 `characters`。

## 板子的版面原則

由左到右就是上課動線，每區一個 `Section`，section 名稱就是區塊標題。

- **卡片區的卡片顏色必須全部統一。** 顏色一旦有差異，就等於暗示分組，整個卡片分類法的效度就沒了。
- **卡片要隨機打散**，不要排成整齊格線——格線本身也是一種分組暗示。
- 需要學生填的地方留空白框（`ShapeWithText` + 虛線 `dashPattern`），並在框裡寫提示。
- 給參考答案的地方，一定要附一張提示便利貼寫「這不是標準答案，優先採用你們自己的結果」。

## 增量建置

一次 `use_figma` 不要超過約 10 個邏輯操作。建完一區就 `await section.screenshot()` 看一眼再往下——座標錯了要早發現，晚發現要重排整批。

每個腳本都要 `return` 建立與修改的 node id。

## 建完之後

把板子連結接回教材：簡報的課堂練習頁與資源頁、練習頁的準備步驟與 foot-nav、講義的實作範本段落與 foot-nav、README 的相關檔案與參考資料。原有的參考板保留為「參考範例」，新板標成「課堂用板」。
