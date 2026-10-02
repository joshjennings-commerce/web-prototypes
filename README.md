# Web prototypes

Shareable, single-file interactive prototypes, published with GitHub Pages from the `docs/` folder.

| Prototype | Live page | Source |
|---|---|---|
| Consolidated navigation concepts | `docs/nav-consolidation/` | `src/nav-consolidation/` |

## Adding a prototype

1. Put the finished page at `docs/<project-name>/index.html` (keep it self-contained: inline CSS, JS, SVGs).
2. Add a card for it in `docs/index.html`.
3. Commit and push — Pages redeploys in about a minute.

## nav-consolidation

`docs/nav-consolidation/index.html` is generated. Edit `src/nav-consolidation/nav-prototype.template.html`, then run:

```
python3 src/nav-consolidation/build.py
```

The gear at the bottom-right of the page opens a control panel; "Copy changes" produces a change list that can be applied back to the `CONTROLS` block in the template.
