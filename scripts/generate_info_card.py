#!/usr/bin/env python3
"""
generate_info_card.py
Renders the "whoami --verbose" terminal panel as an SVG.
Edit the FIELDS dict below with your own info, then re-run this script.
"""
import html

FIELDS = [
    ("Now:", "در حال یادگیری و ساخت پروژه‌های شخصی (placeholder - عوضش کن)"),
    ("Prev:", "— (placeholder - عوضش کن)"),
    ("Stack:", "— (فعلاً خالی، هر وقت مهارتی یاد گرفتی اینجا اضافه کن)"),
    ("Highlights:", "— (placeholder - عوضش کن)"),
    ("Learning:", "Full-Stack Development"),
    ("Reach:", "shop.ario-co.ir - tonystarkicu1@gmail.com"),
]

USERNAME = "AmiryasinYousefi369"
WIDTH = 900
PAD_X = 28
LABEL_X = PAD_X
VALUE_X = 190
LINE_H = 46
TOP_PAD = 70


def build_svg():
    rows = []
    y = TOP_PAD
    for label, value in FIELDS:
        rows.append(f'<text x="{LABEL_X}" y="{y}" class="label">{html.escape(label)}</text>')
        rows.append(f'<text x="{VALUE_X}" y="{y}" class="value">{html.escape(value)}</text>')
        y += LINE_H

    swatches_y = y + 10
    colors = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353", "#58a6ff", "#c9d1d9"]
    swatch_svg = []
    for i, c in enumerate(colors):
        swatch_svg.append(
            f'<rect x="{PAD_X + i*30}" y="{swatches_y}" width="22" height="22" rx="3" fill="{c}" stroke="#30363d"/>'
        )

    footer_y = swatches_y + 50
    height = footer_y + 30

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{height}" viewBox="0 0 {WIDTH} {height}">
  <style>
    .bg {{ fill: #0d1117; }}
    .border {{ fill: none; stroke: #30363d; stroke-width: 1; }}
    .title {{ font-family: 'Courier New', monospace; font-size: 13px; fill: #8b949e; }}
    .user {{ font-family: 'Courier New', monospace; font-size: 15px; font-weight: bold; fill: #39FF14; }}
    .dashes {{ font-family: 'Courier New', monospace; font-size: 13px; fill: #30363d; }}
    .label {{ font-family: 'Courier New', monospace; font-size: 14px; font-weight: bold; fill: #39FF14; }}
    .value {{ font-family: 'Courier New', monospace; font-size: 14px; fill: #c9d1d9; }}
    .footer {{ font-family: 'Courier New', monospace; font-size: 12px; fill: #58a6ff; text-anchor: end; }}
  </style>
  <rect class="bg" width="{WIDTH}" height="{height}" rx="10"/>
  <rect class="border" x="0.5" y="0.5" width="{WIDTH-1}" height="{height-1}" rx="10"/>
  <text x="{PAD_X}" y="30" class="title">{html.escape(USERNAME)}: ~ &#8212; neofetch</text>
  <text x="{PAD_X}" y="{TOP_PAD-24}" class="user">{html.escape(USERNAME)}</text>
  <text x="{PAD_X}" y="{TOP_PAD-10}" class="dashes">------------</text>
  {''.join(rows)}
  {''.join(swatch_svg)}
  <text x="{WIDTH-PAD_X}" y="{footer_y}" class="footer">./whoami --verbose</text>
</svg>"""
    return svg


if __name__ == "__main__":
    svg = build_svg()
    with open("assets/verbose-card.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("verbose-card.svg generated")
