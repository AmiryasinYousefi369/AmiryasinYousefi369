#!/usr/bin/env python3
"""
generate_heatmap.py
Fetches real contribution data for a GitHub user (no token required) and
renders it as a terminal-style heatmap SVG, similar to `contrib-heatmap.svg`.

Data source: https://github-contributions-api.jogruber.de
This is a free public API that mirrors GitHub's contribution graph.
"""
import datetime
import html
import json
import urllib.request

USERNAME = "AmiryasinYousefi369"
API_URL = f"https://github-contributions-api.jogruber.de/v4/{USERNAME}?y=last"

CELL = 11
GAP = 3
LEFT_PAD = 40
TOP_PAD = 40
LEVEL_COLORS = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]


def fetch_contributions():
    try:
        with urllib.request.urlopen(API_URL, timeout=15) as resp:
            data = json.loads(resp.read().decode())
        return data.get("contributions", [])
    except Exception as e:
        print(f"Warning: could not fetch live data ({e}). Using empty calendar.")
        return []


def build_weeks(contributions):
    by_date = {c["date"]: c for c in contributions}
    if contributions:
        last_date = datetime.date.fromisoformat(contributions[-1]["date"])
    else:
        last_date = datetime.date.today()

    end = last_date
    start = end - datetime.timedelta(days=370)
    # align start to a Sunday
    start -= datetime.timedelta(days=(start.weekday() + 1) % 7)

    weeks = []
    cur = start
    week = []
    while cur <= end:
        rec = by_date.get(cur.isoformat())
        level = rec["level"] if rec else 0
        count = rec["count"] if rec else 0
        week.append({"date": cur, "level": level, "count": count})
        if len(week) == 7:
            weeks.append(week)
            week = []
        cur += datetime.timedelta(days=1)
    if week:
        weeks.append(week)
    return weeks


def compute_stats(contributions):
    total = sum(c["count"] for c in contributions)
    current_streak = 0
    longest_streak = 0
    running = 0
    best_day = 0
    for c in contributions:
        if c["count"] > 0:
            running += 1
            longest_streak = max(longest_streak, running)
        else:
            running = 0
        best_day = max(best_day, c["count"])
    for c in reversed(contributions):
        if c["count"] > 0:
            current_streak += 1
        else:
            break
    days = len(contributions) or 1
    per_day = round(total / days, 2)
    return total, current_streak, longest_streak, best_day, per_day


def build_svg(weeks, stats):
    total, cur_streak, longest, best_day, per_day = stats
    width = LEFT_PAD + len(weeks) * (CELL + GAP) + 20
    height = TOP_PAD + 7 * (CELL + GAP) + 80

    cells = []
    month_labels = []
    last_month = None
    for wi, week in enumerate(weeks):
        x = LEFT_PAD + wi * (CELL + GAP)
        first_valid = next((d for d in week if d["date"] is not None), None)
        if first_valid:
            m = first_valid["date"].strftime("%b")
            if m != last_month:
                month_labels.append(f'<text x="{x}" y="20" class="month">{m}</text>')
                last_month = m
        for di, day in enumerate(week):
            y = TOP_PAD + di * (CELL + GAP)
            color = LEVEL_COLORS[min(day["level"], 4)]
            cells.append(
                f'<rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="2" fill="{color}"/>'
            )

    day_labels = f"""
    <text x="4" y="{TOP_PAD + 1*(CELL+GAP) + 8}" class="daylabel">Mon</text>
    <text x="4" y="{TOP_PAD + 3*(CELL+GAP) + 8}" class="daylabel">Wed</text>
    <text x="4" y="{TOP_PAD + 5*(CELL+GAP) + 8}" class="daylabel">Fri</text>
    """

    footer_y = TOP_PAD + 7 * (CELL + GAP) + 30
    stats_line = (
        f"{total} contributions in the last year &#183; "
        f"current streak {cur_streak}d &#183; longest {longest}d &#183; "
        f"best day {best_day} &#183; {per_day}/day"
    )

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <style>
    .bg {{ fill: #0d1117; }}
    .border {{ fill: none; stroke: #30363d; stroke-width: 1; }}
    .title {{ font-family: 'Courier New', monospace; font-size: 13px; fill: #8b949e; }}
    .month {{ font-family: 'Courier New', monospace; font-size: 10px; fill: #8b949e; }}
    .daylabel {{ font-family: 'Courier New', monospace; font-size: 9px; fill: #8b949e; }}
    .stats {{ font-family: 'Courier New', monospace; font-size: 12px; fill: #39FF14; }}
  </style>
  <rect class="bg" width="{width}" height="{height}" rx="10"/>
  <rect class="border" x="0.5" y="0.5" width="{width-1}" height="{height-1}" rx="10"/>
  <text x="20" y="20" class="title">{html.escape(USERNAME)} &#8212; contributions, last 12 months</text>
  {''.join(month_labels)}
  {day_labels}
  {''.join(cells)}
  <text x="20" y="{footer_y}" class="stats">{stats_line}</text>
</svg>"""
    return svg


if __name__ == "__main__":
    contributions = fetch_contributions()
    weeks = build_weeks(contributions)
    stats = compute_stats(contributions)
    svg = build_svg(weeks, stats)
    with open("assets/contrib-heatmap.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("contrib-heatmap.svg generated")
