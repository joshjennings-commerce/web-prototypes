# Web prototypes

Shareable, single-file interactive prototypes, published with GitHub Pages from the repo root.
Each prototype is self-contained in its own folder:

```
<project>/
  index.html   ← the published page  →  https://<user>.github.io/web-prototypes/<project>/
  src/         ← anything used to produce it (templates, assets, build scripts)
```

| Prototype | Folder |
|---|---|
| Consolidated navigation concepts | `nav-consolidation/` |

## Adding a prototype

1. Create `<project>/index.html` (keep it self-contained: inline CSS, JS, SVGs). Put working files in `<project>/src/`.
2. Add a card for it in the root `index.html`.
3. Commit and push — Pages redeploys in about a minute.

## nav-consolidation

`nav-consolidation/index.html` is generated. Edit `nav-consolidation/src/nav-prototype.template.html`, then run:

```
python3 nav-consolidation/src/build.py
```

The gear at the bottom-right of the page opens a control panel; "Copy changes" produces a change list that can be applied back to the `CONTROLS` block in the template.

**Versions and variations.** The bottom-left toolbar has a Version dropdown and Variation buttons. Versions are defined in the `VERSIONS` object in the template; each version holds numbered variations.

| Version | Variations | What changed |
|---|---|---|
| 1.0 | 1–4 | Original combos: Parent A/B (Solutions vs. Platforms dropdown) × Sub-brand A/B (dual nav vs. focused nav with "C" expander) |
| 2.0 | 1–2 | Post-CMO-review: Solutions (brand panels) + Industries top-level, Resources → Learning, sub-brand Resources dropdown, brand-grouped Get Started CTA. Var 1 = CTA dropdown, Var 2 = CTA modal |

Deep links: `#v2.0-1`, `#v1.0-3`, etc. Append `-review` to open with Review mode on.

**Review mode.** The Review toggle in the toolbar outlines flagged nav items in amber with numbered markers (hover or click a marker for the note) and lists all open questions. Flags live in the `FLAGS` object in the template, keyed by version; add or remove entries there.
