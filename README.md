# Dais & Apex brand assets

The studio mark: an interlocked **D** and **A**, the dais, with an orange peak
between the A's legs, the apex.

The master is `assets/da-logo.svg`. It is built from exact lines and arcs: one
2:1 slope for every diagonal, one stroke width, one ring for the D's bowl.
Every raster in `assets/` is rendered from it.

A full brand design pass is under way. The palette, and possibly the shapes,
may change.

## Files

| File | Use |
|------|-----|
| `assets/da-logo.svg` | **Master.** Colour mark, vector. |
| `assets/da-logo-black.svg` | All-black silhouette, vector. Light grounds, print, single ink. |
| `assets/da-logo-white.svg` | All-white silhouette, vector. Dark grounds. |
| `assets/da-logo.png`, `-black.png`, `-white.png` | The same three, 1024 px wide. |
| `assets/avatar-512.png` | GitHub org avatar, white tile. Upload via the web UI. |
| `assets/avatar-circle-512.png` | Black mark on a white disc, for circle crops. |
| `assets/favicon-16/32/48.png` | Raster favicons. |
| `assets/favicon.ico` | Multi-resolution icon (16/32/48) for legacy clients. |
| `assets/da-logo-original.png` | The designer's original raster (158 px), kept for reference. Not for use. |
| `tools/score_mark.py` | Match check for redraws. |

## Palette

| Token | Hex | CSS property | Role |
|-------|-----|--------------|------|
| Structure grey | `#716f6e` | `--da-structure` | The D and A |
| Apex orange | `#e67819` | `--da-apex` | The peak |

In the SVGs the fills come from the two CSS custom properties. Renderers
without CSS support use the plain `fill` attributes, so change both when
recolouring.

## Usage

- Use the SVG wherever it is accepted. For rasters, render from the SVG at the
  size needed rather than scaling a PNG.
- The silhouettes are for single-ink contexts.
- The white channels between the D, the A and the peak are part of the mark.
  Keep them clear.

## Redraws

A redraw may replace the master when it passes the match check against the
original raster:

- IoU of at least 0.98 per colour;
- the white channels clear;
- the same open regions as the original, so no channel closes up.

Render at 158 px and run the check (Pillow only):

```
inkscape --export-type=png --export-width=158 --export-filename=render.png assets/da-logo.svg
python3 tools/score_mark.py render.png
```

The current master scores 0.9963 (structure) and 0.9923 (apex).

## Product marks

The studio mark above identifies **Dais & Apex**. Each product carries its own
mark; the studio logo is never stamped on a product. Brand family comes from
shared restraint and a shared accent, not from repeating the logo.

Snapshots below; each product repo remains canonical.

| Product | Mark | Palette | Status |
|---|---|---|---|
| [demiplane](pillars/demiplane/) | A **pocket reality**: bounded outer world, gateway gap at the bottom, smaller pocket sealed inside. Monochrome single-weight line art; reduces to ASCII. | Ink `#e7e9ec` on dark / `#14171c` on light; tile `#14171c` | Public |
| [fur](pillars/fur/) | A geometric monogram: paired chevrons `>>` / `<<` flanking a bracketed `[ ]` on a solid black tile. Reads as navigation between documents. | Ink `#000000`, Paper `#ffffff`, Signal Pink `#fd578e`, Signal Blue `#52cbfd` | Unreleased |
| Firn | Not yet drawn. Brief exists: metaphor is *frozen in time* (firn is snow that survived an earlier season). Must not resemble the Gradia mark it replaces, must not be the studio logo, no text. | Cold blues/whites with `#e67819` as accent only | Brief only |

### What the aesthetic is, in one paragraph

Line art over illustration. Monochrome by default, with a single saturated
accent used sparingly. Marks are built from geometric primitives that survive
downscaling to 16px, and every one of them is tested there. Nothing decorative:
each mark encodes what the product *does*, a bounded pocket or a bracket
between chevrons, rather than depicting the category it belongs to. No
gradients on flat surfaces, no shadows, no outlines, no rotation, no
stretching.

### For a designer picking this up

Read `pillars/demiplane/README.md` first. It is the most complete expression of
the house style, including how the mark degrades to ASCII. Then `pillars/fur/`
for how the accent pair is handled. Both documents specify clear space, minimum
size, and the exact regeneration pipeline from vector master to raster set;
those conventions carry to any new mark.

The open brief is **Firn**, and it is the real work: a GTK4/libadwaita app icon
that must pass GNOME HIG review and Flathub quality guidelines. The brief lives
outside this repo; ask the studio for it.
