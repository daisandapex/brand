# Dais & Apex — brand assets

The studio mark: an interlocked **D** and **A** — the dais — with a freestanding
peak between the A's legs — the apex. The D's bowl terminates on an angled cut
parallel to the A's leg; the white channel between them is the joint of the
mark, not an accident. Single-color by default; the apex is a separate path
(`id="apex"`) and can take the accent color at any time.

## Files

| File | Use |
|------|-----|
| `assets/da-mark.svg` | **Canonical mark.** `currentColor` — recolors to context. |
| `assets/da-mark-light.svg` | Baked ink for light grounds (`#7d7b7c`). |
| `assets/da-mark-dark.svg` | Baked ink for dark grounds (`#a8aaae`). |
| `assets/da-mark-accent.svg` | Two-tone variant: grey structure, orange apex (`#ea8b1e`). |
| `assets/favicon.svg` | Theme-adaptive favicon (`prefers-color-scheme`). |
| `assets/favicon-tile.svg` | Mark on a dark rounded tile — raster source. |
| `assets/favicon-16/32/48.png`, `favicon.ico` | Raster favicons + legacy multi-res ico. |
| `assets/avatar-512.png` | GitHub org avatar (upload via web UI). |

## Palette

| Token | Hex | Role |
|-------|-----|------|
| Structure (light grounds) | `#7d7b7c` | D + A ink on light |
| Structure (dark grounds) | `#a8aaae` | D + A ink on dark |
| Apex accent | `#ea8b1e` | Optional peak fill (accent variant) |
| Tile | `#101216` | Avatar/favicon ground |

## Usage

- Default is the **single-color** mark; use the accent variant deliberately,
  not as the everyday form.
- To recolor the apex in any context: target `#apex` (it is always its own
  path, even in the single-color files).
- Keep the channels clear — nothing may touch the white gaps between the D,
  the A, and the peak; they are part of the mark.
- Minimum size: the mark holds at 32px; below that, use the tile forms.
