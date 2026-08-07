# Dais & Apex — brand assets

The studio mark: an interlocked **D** and **A** — the dais — with an orange
peak between the A's legs — the apex. Designed by the studio; the master
artwork is the raster original, kept verbatim. Derived files are produced only
by background removal, cropping, recoloring the silhouette, and scaling —
never by redrawing.

## Files

| File | Use |
|------|-----|
| `assets/da-logo.png` | **Master.** Original artwork, transparent background. |
| `assets/da-logo-black.png` | All-black silhouette — light grounds, print, single-ink. |
| `assets/da-logo-white.png` | All-white silhouette — dark grounds. |
| `assets/avatar-512.png` | GitHub org avatar (white tile; upload via web UI). |
| `assets/favicon-16/32/48.png` | Raster favicons, downscaled from the master. |
| `assets/favicon.ico` | Multi-resolution icon (16/32/48) for legacy clients. |

## Palette (sampled from the master)

| Token | Hex | Role |
|-------|-----|------|
| Structure grey | `#716f6e` | The D and A |
| Apex orange | `#e67819` | The peak |

## Usage

- The color master is the default form. Black/white silhouettes are for
  single-ink contexts; they are recolors of the same pixels, not redraws.
- The white channels between the D, the A, and the peak are part of the mark —
  keep them clear.
- The master is 158px wide: fine for avatars and below. For large-format uses,
  regenerate the derived set from a higher-resolution export of the original
  artwork using the same pipeline; do not upscale beyond the avatar size, and
  do not substitute a redrawn version.

## Product marks

The studio mark above identifies **Dais & Apex**. Each product carries its own
mark — the studio logo is never stamped on a product. Brand family comes from
shared restraint and a shared accent, not from repeating the logo.

Snapshots below; each product repo remains canonical.

| Product | Mark | Palette | Status |
|---|---|---|---|
| [demiplane](pillars/demiplane/) | A **pocket reality** — bounded outer world, gateway gap at the bottom, smaller pocket sealed inside. Monochrome single-weight line art; reduces to ASCII. | Ink `#e7e9ec` on dark / `#14171c` on light; tile `#14171c` | Public |
| [fur](pillars/fur/) | A geometric monogram — paired chevrons `>>` / `<<` flanking a bracketed `[ ]` on a solid black tile. Reads as navigation between documents. | Ink `#000000`, Paper `#ffffff`, Signal Pink `#fd578e`, Signal Blue `#52cbfd` | Unreleased |
| Firn | Not yet drawn. Brief exists: metaphor is *frozen in time* (firn is snow that survived an earlier season). Must not resemble the Gradia mark it replaces, must not be the studio logo, no text. | Cold blues/whites with `#e67819` as accent only | Brief only |

### What the aesthetic is, in one paragraph

Line art over illustration. Monochrome by default, with a single saturated
accent used sparingly. Marks are built from geometric primitives that survive
downscaling to 16px, and every one of them is tested there. Nothing decorative:
each mark encodes what the product *does* — a bounded pocket, a bracket between
chevrons — rather than depicting the category it belongs to. No gradients on
flat surfaces, no shadows, no outlines, no rotation, no stretching.

### For a designer picking this up

Read `pillars/demiplane/README.md` first — it is the most complete expression of
the house style, including how the mark degrades to ASCII. Then `pillars/fur/`
for how the accent pair is handled. Both documents specify clear space, minimum
size, and the exact regeneration pipeline from vector master to raster set;
those conventions carry to any new mark.

The open brief is **Firn**, and it is the real work: a GTK4/libadwaita app icon
that must pass GNOME HIG review and Flathub quality guidelines. That brief lives
outside this repo — ask for `prepared/firn/icon-spec.md`.
