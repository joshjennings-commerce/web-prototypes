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
