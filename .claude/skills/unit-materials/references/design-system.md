# 設計系統契約

三份檔案共用同一組色票，各自有固定的骨架。**整段沿用參照單元的 `<style>` 與 `<script>`，只增不改。**

## 色票（三份檔案一致）

```css
--bg: #fbfbfd;      --dark: #1d1d1f;    --muted: #6e6e73;
--accent: #0066cc;  --accent2: #0f766e; --accent3: #c2410c;
--surface: #f5f5f7; --card: #ffffff;    --border: #d2d2d7;
```

`--accent` 主色藍、`--accent2` 綠（正面／回家作業）、`--accent3` 橘（警告／痛點）。深色頁的藍固定用 `#58a6ff`，不是 `--accent`。

字型：`'Inter', -apple-system, BlinkMacSystemFont, "SF Pro Text", "PingFang TC", sans-serif`。

## slides.html

**骨架**：`#prog` 進度條 → `#deck` 內一連串 `<section class="slide">` → `#ctrls` 上下頁按鈕 → `<script>`。

每張投影片固定三段：

```html
<section class="slide">            <!-- 深色頁加 dark -->
  <div class="slide-head"><span class="unit-pill">Unit XX</span><span class="slide-num"></span></div>
  <div class="slide-body"> ... </div>
  <div class="slide-foot"><span class="course-label">單元副標</span><div class="dots"></div></div>
</section>
```

`slide-num` **留空**，由 JS 自動填 `01 / NN`。手動寫死等於埋一顆會在增刪投影片時爆的雷。

**JS 必備行為**：自動編號、圓點導航、進度條、深色頁時 `#ctrls` 加 `on-dark`、`←/→/空白/PageUp/PageDown/Home/End` 鍵。

**深淺交錯**：相鄰投影片不要同色，封面淺、議程深，之後交替。

**可用元件**：`.agenda-grid`／`.agenda-card`、`.blist`（`.plain`／`.compact`）、`.matrix`（`.c3`／`.c4`）、`.mini-card`（`.accent`／`.warn`）、`.cmp-table`、`.chain`（`.c5`）、`.stat-row`、`.note`、`.layer-badge`、`.bg-n`、`.res-links`／`.res-link`。

**行內連結**用 `.ilink`：

```css
.slide-body a.ilink { color: var(--accent); font-weight: 700; text-decoration: none;
                      border-bottom: 1px solid rgba(0,102,204,.35); }
.slide.dark .slide-body a.ilink { color: #58a6ff; border-bottom-color: rgba(88,166,255,.42); }
```

**外部連結**一律 `target="_blank" rel="noopener"`，本地頁面也是——簡報放映中不該跳走。

## article.html

**骨架**：`#prog` → `.side-nav`（`@media (min-width:1400px)` 才顯示）→ `.topbar` → `.hero` → `.toc`（雙欄）→ `.article` 內一連串 `<section class="section" id="sN">` → `.refs` → `.foot-nav` → `<script>`。

每節固定開頭：

```html
<section class="section" id="sN">
  <p class="sec-num">NN</p>
  <h2 class="sec-title">標題</h2>
```

`id="sN"` 的 N 與 `sec-num` 的 NN 要一致。**插入新節時，後面所有節的 id 與 sec-num 一起往後推**，並同步 `.side-nav`、`.toc`，以及其他檔案裡的「第 N 節」。

**JS 必備**：捲動進度條、`IntersectionObserver` 高亮側邊大綱、`.prompt` 的複製按鈕。

**AI 提示詞**放在最後一節，每段包在 `.prompt > pre` 裡並附 `.copy-btn`。提示詞結尾一律加限制句：「只能根據我提供的內容分析，不要自行補充不存在的資訊。」

## exercises.html

**骨架**：`.page` → `.topbar` → `.hero` → `.toc` → 用 `.band` 分隔「課堂練習」與「回家作業」兩區 → `.exercise` 卡片 → `.foot-nav`。

回家作業的卡片加 `.home`（綠色系）與 `.band-tag.home`，跟課堂練習在視覺上分開。

每張練習卡：

```html
<div class="exercise" id="exN">
  <div class="exercise-head">
    <p class="exercise-tag">Exercise 0N</p>
    <h2>標題</h2>
    <div class="meta"><span class="chip">NN 分鐘</span><span class="chip">分組方式</span></div>
  </div>
  <div class="exercise-body"> ... <div class="callout"><strong>交件：</strong>...</div></div>
</div>
```

**必備 id**：`#ex1`…（課堂練習）、`#hw`（回家作業）、`#submit`（繳交清單與配分）——其他檔案會連過來。

`@media print` 要隱藏 `.topbar`、`.toc`、`.foot-nav`，並讓 `.exercise` 不跨頁斷開。

## 三份檔案的連結網

雙向都要有，而且要連到**具體段落**，不是只連檔案：

- 簡報 → 講義小節、練習 `#ex1`／`#hw`／`#submit`、Figma、影片
- 講義 topbar → 簡報；foot-nav → 簡報、`#ex1`、`#hw`、Figma、影片、`../index.html`
- 練習 topbar → 講義；foot-nav → 簡報、講義、講義小節、Figma、影片、`../index.html`
