#!/usr/bin/env python3
"""單元教材驗收腳本。

用法：
    python3 .claude/skills/unit-materials/validate.py Unit_05

檢查 slides.html / article.html / exercises.html 的：
  - HTML 結構、重複 id
  - 內部連結與跨檔錨點
  - 使用但未定義的 CSS class
  - 簡報張數與封面標示是否相符
  - 講義節號是否連續、side-nav 與 TOC 是否對得上
  - 「第 N 節」交叉引用是否指對

另外把所有時間數字列出來，讓你自己對帳（腳本不判對錯）。
"""

import os
import re
import sys
from html.parser import HTMLParser

VOID = {'br', 'img', 'input', 'meta', 'link', 'hr', 'source',
        'area', 'base', 'col', 'embed', 'param', 'track', 'wbr'}

TARGETS = ['slides.html', 'article.html', 'exercises.html']


class Structure(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.errors = []
        self.ids = {}

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if 'id' in d:
            self.ids[d['id']] = self.ids.get(d['id'], 0) + 1
        if tag not in VOID:
            self.stack.append((tag, self.getpos()))

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if not self.stack:
            self.errors.append(f'多餘的 </{tag}> 於 L{self.getpos()[0]}')
            return
        top, pos = self.stack.pop()
        if top != tag:
            self.errors.append(
                f'標籤不匹配：<{top}> (L{pos[0]}) 對到 </{tag}> (L{self.getpos()[0]})')


def read(path):
    with open(path, encoding='utf-8') as fh:
        return fh.read()


def check_file(unit_dir, name, problems, notes):
    path = os.path.join(unit_dir, name)
    if not os.path.exists(path):
        notes.append(f'{name}：不存在，略過')
        return None

    src = read(path)
    parser = Structure()
    parser.feed(src)

    for err in parser.errors:
        problems.append(f'{name}：{err}')
    for tag, pos in parser.stack:
        problems.append(f'{name}：未閉合 <{tag}> 於 L{pos[0]}')
    for key, count in parser.ids.items():
        if count > 1:
            problems.append(f'{name}：重複 id "{key}"（{count} 次）')

    # 連結與錨點
    for href in sorted(set(re.findall(r'href="(?!https?:|mailto:|tel:)([^"]+)"', src))):
        target, _, frag = href.partition('#')
        if target:
            resolved = os.path.normpath(os.path.join(unit_dir, target))
            if not os.path.exists(resolved):
                problems.append(f'{name}：連結失效 "{href}"（找不到 {target}）')
                continue
            other = read(resolved)
        else:
            other = src
        if frag and f'id="{frag}"' not in other:
            problems.append(f'{name}：錨點不存在 "{href}"')

    # CSS class（排除 <script>：JS 會用字串拼接 class，會造成誤報）
    if '<style>' in src:
        css = src.split('<style>')[1].split('</style>')[0]
        defined = set(re.findall(r'\.([a-zA-Z][\w-]*)', css))
        markup = re.sub(r'<script.*?</script>', ' ', src, flags=re.S)
        used = set()
        for attr in re.findall(r'class="([^"]+)"', markup):
            used.update(attr.split())
        missing = sorted(used - defined)
        if missing:
            problems.append(f'{name}：使用但未定義的 class {missing}')

    # 時間數字（僅列出，不判對錯）
    times = re.findall(r'[^\w]([0-9]{1,3})\s*(?:分鐘|分(?![a-zA-Z])|min\b|mins\b)', src)
    if times:
        notes.append(f'{name}：出現的時間數字 → {", ".join(times)}')

    return src


def check_slides(src, problems, notes):
    if src is None:
        return
    classes = re.findall(r'<(?:section|div) class="(slide(?:\s[^"]*)?)"', src)
    total = len(classes)
    # 標了 drop 的是備用頁，CSS 隱藏、翻頁 JS 也跳過，不算進會播的張數
    dropped = sum(1 for c in classes if 'drop' in c.split())
    slides = total - dropped
    if dropped:
        notes.append(f'slides.html：投影片 {slides} 張（另有 {dropped} 張標了 drop 的備用頁，不列入計數）')
    else:
        notes.append(f'slides.html：投影片 {slides} 張')
    declared = re.findall(r'([0-9]{1,3})\s*張投影片', src)
    for d in set(declared):
        if int(d) != slides:
            problems.append(
                f'slides.html：封面寫「{d} 張投影片」，實際會播 {slides} 張')
    if re.search(r'class="slide-num">\s*\d', src):
        notes.append('slides.html：slide-num 是寫死的（舊版寫法）。新做的簡報請留空，改由 JS 自動編號')
    for tag in re.findall(r'<a\b[^>]*href="https?://[^"]*"[^>]*>', src):
        if 'target="_blank"' not in tag:
            problems.append(f'slides.html：外部連結缺 target="_blank" → {tag[:70]}')


def check_article(unit_dir, src, problems, notes):
    if src is None:
        return
    if 'class="section"' not in src:
        notes.append('article.html：未使用現行的 .section / #sN 結構（舊版單元），跳過節號檢查')
        return
    nums = re.findall(r'<p class="sec-num">[^<\d]*(\d+)\s*</p>', src)
    ids = re.findall(r'<(?:section|div) class="section" id="s(\d+)"', src)
    notes.append(f'article.html：{len(nums)} 節')

    expected = [f'{i:02d}' for i in range(1, len(nums) + 1)]
    if nums != expected:
        problems.append(f'article.html：sec-num 不連續 → {nums}')
    if [int(x) for x in ids] != list(range(1, len(ids) + 1)):
        problems.append(f'article.html：section id 不連續 → {ids}')
    if len(nums) != len(ids):
        problems.append(
            f'article.html：sec-num 有 {len(nums)} 個，section id 有 {len(ids)} 個')

    for label, block in (('side-nav', r'<nav class="side-nav".*?</nav>'),
                         ('toc', r'<div class="toc">.*?</div>')):
        m = re.search(block, src, re.S)
        if not m:
            problems.append(f'article.html：找不到 {label}')
            continue
        anchors = re.findall(r'href="#s(\d+)"', m.group(0))
        if [int(a) for a in anchors] != [int(i) for i in ids]:
            problems.append(
                f'article.html：{label} 的錨點與實際小節對不上 → {anchors} vs {ids}')

    # 其他檔案裡的「講義第 N 節」
    titles = re.findall(r'<h2 class="sec-title">([^<]+)</h2>', src)
    for name in TARGETS + ['README.md']:
        path = os.path.join(unit_dir, name)
        if not os.path.exists(path):
            continue
        for ref in re.findall(r'講義第\s*(\d+)\s*節', read(path)):
            n = int(ref)
            if not 1 <= n <= len(titles):
                problems.append(f'{name}：引用「講義第 {ref} 節」，但講義只有 {len(titles)} 節')
            else:
                notes.append(f'{name}：引用「講義第 {ref} 節」→ 目前是「{titles[n - 1]}」，請確認語意相符')


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2

    unit_dir = sys.argv[1].rstrip('/')
    if not os.path.isdir(unit_dir):
        print(f'找不到資料夾：{unit_dir}')
        return 2

    problems, notes = [], []
    sources = {}
    for name in TARGETS:
        sources[name] = check_file(unit_dir, name, problems, notes)

    check_slides(sources.get('slides.html'), problems, notes)
    check_article(unit_dir, sources.get('article.html'), problems, notes)

    print(f'=== {unit_dir} ===\n')
    if notes:
        print('— 對帳報表（腳本不判對錯，請自行確認）—')
        for n in notes:
            print(f'  · {n}')
        print()

    if problems:
        print(f'— 問題 {len(problems)} 項 —')
        for p in problems:
            print(f'  ✗ {p}')
        return 1

    print('✓ 結構、連結、錨點、class、編號全部通過')
    return 0


if __name__ == '__main__':
    sys.exit(main())
