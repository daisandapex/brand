#!/usr/bin/env python3
"""Check a redraw of the studio mark against the original raster.

The original (assets/da-logo-original.png, 158x112) has binary alpha; its
edge pixels are the mark's colour blended toward white. Each pixel's
coverage of the structure grey and the apex orange is recovered from that
blend. The candidate is a 158x112 render with a transparent background and
is read the same way, against its own two fill colours; for a vector
render with exact fills that is simply its alpha.

Pass criteria:
  * IoU of at least 0.98 per colour (masks cut at 50% coverage);
  * the white channels clear: no candidate pixel above alpha 64 where the
    original is transparent inside the mark's bounding box;
  * the same number of open background regions as the original.

Pixel match on white is reported for information. A crisp vector scores
about 95% within a tolerance of 16 because the original's edges are softer
than vector anti-aliasing; it is not a pass criterion.

Usage:
  inkscape --export-type=png --export-width=158 --export-filename=r.png assets/da-logo.svg
  python3 tools/score_mark.py r.png [--original assets/da-logo-original.png]
      [--structure '#716f6e'] [--apex '#e67819']

--structure and --apex name the candidate's fill colours, so a recoloured
redraw can be checked against the original's shapes. Requires Pillow only.
Exit status 0 on pass, 1 on fail.
"""

import argparse
import sys
from collections import deque
from pathlib import Path

from PIL import Image

ORIGINAL_STRUCTURE = (0x71, 0x6F, 0x6E)
ORIGINAL_APEX = (0xE6, 0x78, 0x19)
RGB = tuple[int, int, int]
Grid = list[list[float]]
DEFAULT_ORIGINAL = (
    Path(__file__).resolve().parent.parent / "assets" / "da-logo-original.png"
)


def hex_rgb(s: str) -> RGB:
    s = s.lstrip("#")
    return tuple(int(s[i : i + 2], 16) for i in (0, 2, 4))


def blend_coverage(rgb: RGB, colour: RGB) -> tuple[float, float]:
    """Least-squares c in rgb = c*colour + (1-c)*white, plus the residual."""
    d = [255 - k for k in colour]
    c = sum((255 - v) * dk for v, dk in zip(rgb, d)) / sum(dk * dk for dk in d)
    c = min(max(c, 0.0), 1.0)
    resid = sum((v - (255 - c * dk)) ** 2 for v, dk in zip(rgb, d))
    return c, resid


def coverage(img: Image.Image, structure: RGB, apex: RGB) -> tuple[Grid, Grid]:
    """Coverage maps (structure, apex): alpha times the blend toward white.
    A vector render with exact fills gets its alpha; a raster with opaque
    white-blended edges, like the original, gets the blend."""
    w, h = img.size
    px = img.load()
    s = [[0.0] * w for _ in range(h)]
    a = [[0.0] * w for _ in range(h)]
    for y in range(h):
        for x in range(w):
            r, g, b, al = px[x, y]
            if al == 0:
                continue
            cs, rs = blend_coverage((r, g, b), structure)
            ca, ra = blend_coverage((r, g, b), apex)
            if rs <= ra:
                s[y][x] = cs * al / 255
            else:
                a[y][x] = ca * al / 255
    return s, a


def iou(m: Grid, c: Grid) -> float:
    inter = union = 0
    for rm, rc in zip(m, c):
        for vm, vc in zip(rm, rc):
            bm, bc = vm >= 0.5, vc >= 0.5
            inter += bm and bc
            union += bm or bc
    return inter / union if union else 1.0


def regions(empty: list[list[bool]]) -> int:
    """Count 4-connected regions of True cells."""
    h, w = len(empty), len(empty[0])
    seen = [[False] * w for _ in range(h)]
    n = 0
    for y0 in range(h):
        for x0 in range(w):
            if not empty[y0][x0] or seen[y0][x0]:
                continue
            n += 1
            q = deque([(x0, y0)])
            seen[y0][x0] = True
            while q:
                x, y = q.popleft()
                for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if (
                        0 <= nx < w
                        and 0 <= ny < h
                        and empty[ny][nx]
                        and not seen[ny][nx]
                    ):
                        seen[ny][nx] = True
                        q.append((nx, ny))
    return n


def over_white(p: tuple[int, int, int, int]) -> tuple[float, float, float]:
    r, g, b, a = p
    t = a / 255
    return (r * t + 255 * (1 - t), g * t + 255 * (1 - t), b * t + 255 * (1 - t))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("candidate", help="158x112 PNG render of the redraw")
    ap.add_argument("--original", default=str(DEFAULT_ORIGINAL))
    ap.add_argument("--structure", default="#716f6e")
    ap.add_argument("--apex", default="#e67819")
    args = ap.parse_args()

    orig = Image.open(args.original).convert("RGBA")
    cand = Image.open(args.candidate).convert("RGBA")
    if cand.size != orig.size:
        sys.exit(
            f"candidate is {cand.size[0]}x{cand.size[1]}; render it at {orig.size[0]}x{orig.size[1]}"
        )
    w, h = orig.size
    ms, ma = coverage(orig, ORIGINAL_STRUCTURE, ORIGINAL_APEX)
    cs, ca = coverage(cand, hex_rgb(args.structure), hex_rgb(args.apex))
    iou_s, iou_a = iou(ms, cs), iou(ma, ca)

    op, cp = orig.load(), cand.load()
    xs = [x for x in range(w) for y in range(h) if op[x, y][3]]
    ys = [y for x in range(w) for y in range(h) if op[x, y][3]]
    x0, x1, y0, y1 = min(xs), max(xs), min(ys), max(ys)
    channel = blocked = 0
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            if op[x, y][3] == 0:
                channel += 1
                blocked += cp[x, y][3] > 64
    reg_o = regions([[ms[y][x] + ma[y][x] < 0.5 for x in range(w)] for y in range(h)])
    reg_c = regions([[cp[x, y][3] < 128 for x in range(w)] for y in range(h)])
    match = sum(
        max(abs(u - v) for u, v in zip(over_white(op[x, y]), over_white(cp[x, y])))
        <= 16
        for y in range(h)
        for x in range(w)
    ) / (w * h)

    ok = iou_s >= 0.98 and iou_a >= 0.98 and blocked == 0 and reg_o == reg_c
    print(f"IoU structure      {iou_s:.4f}  (bar 0.98)")
    print(f"IoU apex           {iou_a:.4f}  (bar 0.98)")
    print(f"channel pixels     {blocked} of {channel} above alpha 64  (bar 0)")
    print(f"open regions       {reg_c} candidate, {reg_o} original")
    print(f"match on white     {match * 100:.1f}% within 16  (information only)")
    print("PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
