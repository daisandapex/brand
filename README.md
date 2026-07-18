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
