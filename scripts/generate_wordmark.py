#!/usr/bin/env python3
"""
generate_wordmark.py
Renders the ASCII wordmark (AMIRYASIN) as a terminal-style SVG card.
Run manually whenever you want to change the displayed name.
"""
import html

NAME = "AMIRYASIN"
ROLE = "LEARNING & BUILDING"
STATUS = "ONLINE"

# Pre-rendered block-ASCII text for the wordmark (monospace grid of $ / + / space)
ASCII_ART = r"""
  +$$+   $$$  $$+ +$$$$$+  $$$$$$  +$+   $$   +$$+    $$$$$+  +$$$$$+  $$+  $$
  $$+$   $$$++$$+   +$$    $$  +$$  +$$ $$    $$+$   +$$        +$+    $$$  $$
 +$+ $$  $$ $$ $+   +$+    $$$$$+     $$$    +$+ $$   ++$$$+    +$+    $++$ $$
 $$++$$+ $$    $+   +$$    $$  $$     +$+    $$++$$+      $$    +$+    $+ +$$$
$$    $$ $$    $+ +$$$$$+  $$   $$    +$+   +$    $$ +$$$$$+  +$$$$$+  $+  +$$
""".strip("\n").split("\n")

CHAR_W = 8.6
CHAR_H = 15
PAD_X = 24
PAD_Y = 24
WIDTH = int(max(len(l) for l in ASCII_ART) * CHAR_W + PAD_X * 2)
LINE_START_Y = 70


def build_svg():
    lines_svg = []
    for i, line in enumerate(ASCII_ART):
        y = LINE_START_Y + i * CHAR_H
        lines_svg.append(
            f'<text x="{PAD_X}" y="{y}" class="ascii">{html.escape(line)}</text>'
        )
    height = LINE_START_Y + len(ASCII_ART) * CHAR_H + 60

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{height}" viewBox="0 0 {WIDTH} {height}">
  <style>
    .bg {{ fill: #0d1117; }}
    .border {{ fill: none; stroke: #30363d; stroke-width: 1; }}
    .ascii {{ font-family: 'Courier New', monospace; font-size: 13px; fill: #39FF14; white-space: pre; }}
    .label {{ font-family: 'Courier New', monospace; font-size: 12px; fill: #58a6ff; }}
    .name {{ font-family: 'Courier New', monospace; font-size: 16px; font-weight: bold; fill: #ffffff; }}
    .meta {{ font-family: 'Courier New', monospace; font-size: 12px; fill: #8b949e; }}
    .status {{ font-family: 'Courier New', monospace; font-size: 12px; fill: #39FF14; }}
  </style>
  <rect class="bg" width="{WIDTH}" height="{height}" rx="10"/>
  <rect class="border" x="0.5" y="0.5" width="{WIDTH-1}" height="{height-1}" rx="10"/>
  <text x="{PAD_X}" y="30" class="label">WORDMARK.SH / --NAME {html.escape(NAME)}</text>
  {''.join(lines_svg)}
  <text x="{PAD_X}" y="{height-34}" class="name">{html.escape(NAME)}</text>
  <text x="{PAD_X}" y="{height-14}" class="meta">{html.escape(ROLE)}</text>
  <text x="{WIDTH-PAD_X-90}" y="{height-14}" class="status">{html.escape(STATUS)} \u25cf</text>
</svg>"""
    return svg


if __name__ == "__main__":
    svg = build_svg()
    with open("assets/wordmark.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("wordmark.svg generated")
