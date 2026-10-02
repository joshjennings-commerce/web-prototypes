"""Inline the brand logos into the template and write the publishable page.

    python3 src/nav-consolidation/build.py      (run from the repo root)

Edit nav-prototype.template.html, not docs/nav-consolidation/index.html — the latter is generated.
"""
import re, pathlib
HERE = pathlib.Path(__file__).parent
OUT = HERE.parent.parent / 'docs' / 'nav-consolidation' / 'index.html'
L = HERE / 'logos'

def strip_dims(tag):
    return re.sub(r'\s(width|height)="[^"]*"', '', tag, count=2)

c = (L / 'commerce-logo.svg').read_text().strip()
c = re.sub(r'^<svg[^>]*>', lambda m: strip_dims(m.group(0)), c).replace('<svg ', '<svg aria-label="Commerce" ', 1)

b = (L / 'bigcommerce-black.svg').read_text()
b = re.sub(r'<\?xml[^>]*\?>', '', b)
b = re.sub(r'<defs>.*?</defs>', '', b, flags=re.S)
b = re.sub(r'<title>.*?</title>', '', b, flags=re.S)
b = b.replace(' id="Art"', '').replace('class="cls-1"', 'fill="currentColor"')
b = re.sub(r'\s+', ' ', b).replace('> <', '><').strip().replace('<svg ', '<svg aria-label="BigCommerce" ', 1)

f = (L / 'feedonomics-logo.svg').read_text().strip()
f = re.sub(r'^<svg[^>]*>', lambda m: strip_dims(m.group(0)), f)
f = re.sub(r'<g clip-path="[^"]*">', '<g>', f)
f = re.sub(r'<defs>.*?</defs>', '', f, flags=re.S)
f = re.sub(r'\s+', ' ', f).replace('> <', '><').strip().replace('<svg ', '<svg aria-label="Feedonomics" ', 1)

for s in (c, b, f):
    assert '`' not in s and '${' not in s

t = (HERE / 'nav-prototype.template.html').read_text()
out = t.replace('{{SVG_COMMERCE}}', c).replace('{{SVG_BC}}', b).replace('{{SVG_FDX}}', f)
assert '{{SVG_' not in out
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(out)
print(f'wrote {OUT.relative_to(HERE.parent.parent)} ({len(out):,} bytes)')
