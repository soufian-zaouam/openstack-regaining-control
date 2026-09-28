"""Mini-visuals for the KPI cards: small SVGs generated from signals/*.yaml `visual`.

Every visual is drawn in a 320 × 110 box and scaled by its container through the
viewBox, so the same SVG serves the LinkedIn card and the PDF page. Text inside
the SVG is kept to a minimum (the label lives in the card's HTML), marks are
thin, colours come from the CSS variables of tokens.css. The series are
illustrative shapes, not measurements.
"""
from __future__ import annotations

W, H = 320, 110
PAD_L, PAD_R, PAD_T, PAD_B = 6, 6, 8, 10


def _scale(values, lo=None, hi=None, top=PAD_T, bottom=H - PAD_B):
    lo = min(values) if lo is None else lo
    hi = max(values) if hi is None else hi
    rng = (hi - lo) or 1
    n = len(values)
    pts = []
    for i, v in enumerate(values):
        x = PAD_L + (i / max(n - 1, 1)) * (W - PAD_L - PAD_R)
        y = bottom - ((v - lo) / rng) * (bottom - top)
        pts.append((x, y))
    return pts


def _poly(pts, color, width=2.2, dash=None, opacity=1.0):
    d = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<polyline points="{d}" fill="none" stroke="var(--{color})" stroke-width="{width}" '
            f'stroke-linejoin="round" stroke-linecap="round" opacity="{opacity}"{dash_attr}/>')


def _area(pts, color, bottom=H - PAD_B):
    d = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    return (f'<polygon points="{pts[0][0]:.1f},{bottom} {d} {pts[-1][0]:.1f},{bottom}" '
            f'fill="var(--{color}-soft)"/>')


def _dot(x, y, color, r=4):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="var(--{color})"/>'


def _baseline():
    return f'<line x1="{PAD_L}" y1="{H - PAD_B}" x2="{W - PAD_R}" y2="{H - PAD_B}" stroke="var(--rule)" stroke-width="1"/>'


def _text(x, y, s, color="fg-muted", size=11, anchor="start", weight=500):
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-family="IBM Plex Mono, monospace" font-size="{size}" '
            f'font-weight="{weight}" fill="var(--{color})" text-anchor="{anchor}">{s}</text>')


def _wrap(inner: str, aria: str = "") -> str:
    return (f'<svg viewBox="0 0 {W} {H}" width="100%" preserveAspectRatio="xMidYMid meet" '
            f'role="img" aria-label="{aria}">{inner}</svg>')


# --- kinds ---------------------------------------------------------------------

def line_rising(v):
    s = v["series"]
    thr = v.get("threshold")
    lo, hi = min(s) * 0.9, max(max(s), thr or 0) * 1.05
    pts = _scale(s, lo, hi)
    out = [_baseline(), _area(pts, "tech"), _poly(pts, "tech"), _dot(*pts[-1], "tech")]
    if thr:
        ty = _scale([thr], lo, hi)[0][1]
        out.append(f'<line x1="{PAD_L}" y1="{ty:.1f}" x2="{W-PAD_R}" y2="{ty:.1f}" stroke="var(--ops)" stroke-width="1.4" stroke-dasharray="4 4"/>')
        out.append(_text(W - PAD_R, ty - 5, "threshold", "ops", 10, "end"))
    return _wrap("".join(out), v.get("label", ""))


def step_rising(v):
    s = v["series"]
    ev = v.get("event_at", 0)
    pts = _scale(s, 0, max(s) * 1.08)
    # step path
    path = []
    for i, (x, y) in enumerate(pts):
        if i == 0:
            path.append(f"M{x:.1f},{y:.1f}")
        else:
            px, py = pts[i - 1]
            path.append(f"H{x:.1f} V{y:.1f}")
    out = [_baseline(),
           f'<path d="{" ".join(path)}" fill="none" stroke="var(--ops)" stroke-width="2.2" stroke-linejoin="round"/>',
           _dot(*pts[-1], "ops")]
    if 0 < ev < len(pts):
        ex = pts[ev][0]
        out.append(f'<line x1="{ex:.1f}" y1="{PAD_T}" x2="{ex:.1f}" y2="{H-PAD_B}" stroke="var(--risk)" stroke-width="1.4" stroke-dasharray="3 4"/>')
        out.append(_text(ex + 5, PAD_T + 9, "network event", "risk", 10))
    return _wrap("".join(out), v.get("label", ""))


def host_grid(v):
    down = set(v.get("reported_down", []))
    cols, rows = 8, 3
    cw, ch, gap = 34, 22, 5
    x0 = (W - (cols * cw + (cols - 1) * gap)) / 2
    y0 = 4
    out = []
    n = 0
    for r in range(rows):
        for c in range(cols):
            x = x0 + c * (cw + gap)
            y = y0 + r * (ch + gap)
            if n in down:
                out.append(f'<rect x="{x}" y="{y}" width="{cw}" height="{ch}" rx="3" fill="var(--ops-soft)" stroke="var(--ops)" stroke-width="1.4" stroke-dasharray="3 3"/>')
                out.append(_text(x + cw / 2, y + ch / 2 + 4, "?", "ops", 12, "middle", 600))
            else:
                out.append(f'<rect x="{x}" y="{y}" width="{cw}" height="{ch}" rx="3" fill="var(--tech-soft)" stroke="var(--tech)" stroke-width="1"/>')
            n += 1
    ly = y0 + rows * (ch + gap) + 6
    out.append(f'<rect x="{x0}" y="{ly}" width="12" height="9" rx="2" fill="var(--tech-soft)" stroke="var(--tech)"/>')
    out.append(_text(x0 + 18, ly + 8, "reported up", "fg-muted", 10))
    out.append(f'<rect x="{x0 + 110}" y="{ly}" width="12" height="9" rx="2" fill="var(--ops-soft)" stroke="var(--ops)" stroke-dasharray="2 2"/>')
    out.append(_text(x0 + 128, ly + 8, "reported down, host reachable", "fg-muted", 10))
    return _wrap("".join(out), v.get("label", ""))


def cluster_flow(v):
    nodes = int(v.get("nodes", 3))
    out = []
    cx0, cy, r = 26, 30, 14
    for i in range(nodes):
        cx = cx0 + i * 48
        if i < nodes - 1:
            out.append(f'<line x1="{cx + r}" y1="{cy}" x2="{cx + 48 - r}" y2="{cy}" stroke="var(--rule)" stroke-width="2"/>')
        out.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="var(--ink-2)" stroke="var(--tech)" stroke-width="1.6"/>')
        out.append(_text(cx, cy + 4, f"n{i+1}", "tech", 10, "middle", 600))
    out.append(_text(cx0 - r, cy + 30, "primary component · 3 of 3", "fg-muted", 10))
    # flow-control pauses timeline
    ty = 84
    out.append(_text(PAD_L, ty - 8, "writes this week", "fg-muted", 10))
    out.append(f'<rect x="{PAD_L}" y="{ty}" width="{W - PAD_L - PAD_R}" height="10" rx="2" fill="var(--tech-soft)"/>')
    pauses = int(v.get("pauses", 3))
    for i in range(pauses):
        px = PAD_L + 40 + i * 95
        out.append(f'<rect x="{px}" y="{ty}" width="18" height="10" rx="2" fill="var(--ops)"/>')
    out.append(_text(W - PAD_R, ty - 8, f"flow control paused ×{pauses}", "ops", 10, "end"))
    # growth
    out.append(_text(W - PAD_R, cy - 2, v.get("growth", ""), "fg", 11, "end", 600))
    out.append(_text(W - PAD_R, cy + 12, "unarchived rows", "fg-muted", 10, "end"))
    return _wrap("".join(out), v.get("label", ""))


def stacked_outcomes(v):
    ok, err = v["success"], v["error"]
    n = len(ok)
    bw, gap = 26, 12
    x0 = (W - (n * bw + (n - 1) * gap)) / 2
    top, bottom = PAD_T + 4, H - PAD_B
    out = [_baseline()]
    for i in range(n):
        tot = ok[i] + err[i]
        hgt = bottom - top
        h_err = hgt * err[i] / tot
        h_ok = hgt - h_err - 2
        x = x0 + i * (bw + gap)
        out.append(f'<rect x="{x}" y="{bottom - h_ok}" width="{bw}" height="{h_ok}" rx="2" fill="var(--tech-soft)" stroke="var(--tech)" stroke-width="1"/>')
        out.append(f'<rect x="{x}" y="{top}" width="{bw}" height="{h_err}" rx="2" fill="var(--risk-soft)" stroke="var(--risk)" stroke-width="1"/>')
    out.append(_text(x0, H - 1, "success", "tech", 10))
    out.append(_text(W - PAD_R, H - 1, f"error {err[-1]} %", "risk", 10, "end"))
    return _wrap("".join(out), v.get("label", ""))


def headroom_projection(v):
    used = v["used"]
    n1 = v.get("n_plus_one", 88)
    lo, hi = 0, 100
    pts = _scale(used, lo, hi)
    out = [_baseline(), _area(pts, "tech"), _poly(pts, "tech"), _dot(*pts[-1], "tech")]
    ny = _scale([n1], lo, hi)[0][1]
    out.append(f'<line x1="{PAD_L}" y1="{ny:.1f}" x2="{W-PAD_R}" y2="{ny:.1f}" stroke="var(--ops)" stroke-width="1.4" stroke-dasharray="4 4"/>')
    out.append(_text(PAD_L + 2, ny - 5, "N+1 limit", "ops", 10))
    # projection: extend the last slope until it crosses N+1
    (x1, y1), (x2, y2) = pts[-2], pts[-1]
    slope = (y2 - y1) / (x2 - x1) if x2 != x1 else 0
    if slope < 0:
        xc = x2 + (ny - y2) / slope
        out.append(f'<line x1="{x2:.1f}" y1="{y2:.1f}" x2="{min(xc, W-PAD_R):.1f}" y2="{ny:.1f}" stroke="var(--tech)" stroke-width="1.6" stroke-dasharray="3 4"/>')
        out.append(_dot(min(xc, W - PAD_R), ny, "risk", 4))
    out.append(_text(W - PAD_R, H - 1, f"saturation in {v.get('saturation_in', '')}", "risk", 10, "end"))
    out.append(_text(PAD_L, H - 1, "used", "tech", 10))
    return _wrap("".join(out), v.get("label", ""))


def fill_gauge(v):
    fill = float(v.get("fill", 80)); nf = float(v.get("nearfull", 85)); fu = float(v.get("full", 95))
    x0, x1, y, h = PAD_L, W - PAD_R, 24, 16
    scale = lambda p: x0 + (x1 - x0) * p / 100
    out = [f'<rect x="{x0}" y="{y}" width="{x1 - x0}" height="{h}" rx="3" fill="var(--neutral-soft)"/>',
           f'<rect x="{x0}" y="{y}" width="{scale(fill) - x0:.1f}" height="{h}" rx="3" fill="var(--ops)"/>']
    for p, lab, col in ((nf, "nearfull", "ops"), (fu, "full", "risk")):
        px = scale(p)
        out.append(f'<line x1="{px:.1f}" y1="{y - 6}" x2="{px:.1f}" y2="{y + h + 6}" stroke="var(--{col})" stroke-width="1.6"/>')
    out.append(_text(scale(nf) - 4, y + h + 18, f"nearfull {int(nf)} %", "ops", 10, "end"))
    out.append(_text(x1, y - 8, f"full {int(fu)} %", "risk", 10, "end"))
    out.append(_text(x0, y - 8, f"fill {int(fill)} %", "fg", 11, "start", 600))
    # latency sparkline in the lower half
    lt = v.get("latency_trend", [])
    if lt:
        pts = _scale(lt, min(lt) * 0.8, max(lt) * 1.1, top=70, bottom=H - PAD_B)
        out.append(_poly(pts, "tech"))
        out.append(_dot(*pts[-1], "tech"))
        out.append(_text(x0, 74, "client i/o latency ↑", "tech", 10, "start"))
    return _wrap("".join(out), v.get("label", ""))


def loss_spikes(v):
    s = v["series"]
    n = len(s)
    bw = (W - PAD_L - PAD_R) / n - 4
    top, bottom = PAD_T + 4, 66
    hi = max(s) or 1
    out = [f'<line x1="{PAD_L}" y1="{bottom}" x2="{W-PAD_R}" y2="{bottom}" stroke="var(--rule)" stroke-width="1"/>']
    for i, val in enumerate(s):
        x = PAD_L + i * (bw + 4)
        h = (bottom - top) * val / hi
        col = "risk" if val >= 1.5 else "tech"
        out.append(f'<rect x="{x:.1f}" y="{bottom - max(h, 1.5):.1f}" width="{bw:.1f}" height="{max(h, 1.5):.1f}" rx="1.5" fill="var(--{col})" opacity="{0.9 if val else 0.35}"/>')
    out.append(_text(PAD_L, top + 2, "packet loss between nodes", "fg-muted", 10))
    # agents
    tot, flap = int(v.get("agents_total", 12)), int(v.get("agents_flapping", 3))
    ay = 92
    for i in range(tot):
        cx = PAD_L + 7 + i * 15
        col = "ops" if i in (2, 6, 9) and flap else "tech"
        out.append(f'<circle cx="{cx}" cy="{ay}" r="4.5" fill="var(--{col})"/>')
    out.append(_text(PAD_L + 7 + tot * 15 + 4, ay + 4, f"agents · {flap} flapping", "fg-muted", 10))
    return _wrap("".join(out), v.get("label", ""))


def reported_vs_actual(v):
    rows = v["rows"]
    out = []
    y = 8
    maxv = max(max(int(r[1]), int(r[2])) for r in rows)
    lab_w = 110
    bar_w = W - PAD_R - lab_w - 60
    for name, rep, act in rows:
        rep, act = int(rep), int(act)
        out.append(_text(PAD_L, y + 12, name, "fg-muted", 10))
        out.append(f'<rect x="{lab_w}" y="{y}" width="{bar_w * rep / maxv:.1f}" height="7" rx="1.5" fill="var(--neutral-soft)" stroke="var(--neutral)" stroke-width="0.8"/>')
        out.append(f'<rect x="{lab_w}" y="{y + 10}" width="{bar_w * act / maxv:.1f}" height="7" rx="1.5" fill="var(--tech)"/>')
        out.append(_text(W - PAD_R, y + 13, f"−{rep - act}", "ops", 11, "end", 600))
        y += 28
    out.append(f'<rect x="{lab_w}" y="{y + 2}" width="10" height="6" fill="var(--neutral-soft)" stroke="var(--neutral)" stroke-width="0.8"/>')
    out.append(_text(lab_w + 15, y + 8, "reported", "fg-muted", 10))
    out.append(f'<rect x="{lab_w + 80}" y="{y + 2}" width="10" height="6" fill="var(--tech)"/>')
    out.append(_text(lab_w + 95, y + 8, "verified", "fg-muted", 10))
    return _wrap("".join(out), v.get("label", ""))


def two_trends(v):
    a, b = v["time_to_understand"], v["recurring"]
    pa = _scale(a, 0, max(a) * 1.1, top=PAD_T + 6, bottom=H - PAD_B)
    pb = _scale(b, 0, max(b) * 1.1, top=PAD_T + 6, bottom=H - PAD_B)
    out = [_baseline(), _poly(pa, "ops"), _dot(*pa[-1], "ops"), _poly(pb, "risk", dash="4 3"), _dot(*pb[-1], "risk")]
    out.append(_text(PAD_L, PAD_T + 4, "time to understand ↑", "ops", 10))
    out.append(_text(W - PAD_R, PAD_T + 4, "recurring incidents ↑", "risk", 10, "end"))
    out.append(_text(PAD_L, H - 1, "Q1", "fg-muted", 10))
    out.append(_text(W - PAD_R, H - 1, "Q5", "fg-muted", 10, "end"))
    return _wrap("".join(out), v.get("label", ""))


KINDS = {
    "line-rising": line_rising,
    "step-rising": step_rising,
    "host-grid": host_grid,
    "cluster-flow": cluster_flow,
    "stacked-outcomes": stacked_outcomes,
    "headroom-projection": headroom_projection,
    "fill-gauge": fill_gauge,
    "loss-spikes": loss_spikes,
    "reported-vs-actual": reported_vs_actual,
    "two-trends": two_trends,
}


def render_visual(v: dict) -> str:
    fn = KINDS.get(v.get("kind"))
    if not fn:
        return _wrap(_baseline(), v.get("label", ""))
    return fn(v)
