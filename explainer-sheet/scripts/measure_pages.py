#!/usr/bin/env python3
"""Measure an explainer sheet against a page budget.

Renders the HTML at true print column width, reports the height of every
.sec block, the total, and how many pages that needs. Also renders the PDF
and reports the real page count, since break-avoidance rules mean the two
numbers differ.

    python measure_pages.py sheet.html
    python measure_pages.py sheet.html --width 703 --budget 1047
    python measure_pages.py sheet.html --sweep 1.0 1.1 1.2 1.3

Defaults are A4 portrait with 10/12/8/12mm margins:
    content width  186mm = 703px
    content height 277mm = 1047px
A4 landscape is --width 1032 --budget 726.
"""
import argparse, pathlib, re, sys

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sys.exit("pip install playwright && playwright install chromium")


def measure(path, width, budget):
    url = pathlib.Path(path).absolute().as_uri()
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": width, "height": budget})
        pg.goto(url)
        pg.emulate_media(media="print")
        pg.wait_for_timeout(400)
        secs = pg.evaluate("""() => [...document.querySelectorAll('.sec')].map(c => [
            (c.querySelector('h1,h2,h3')?.textContent || '(untitled)').slice(0, 44),
            Math.round(c.getBoundingClientRect().height),
            Math.round(c.scrollWidth)])""")
        pg.pdf(path="/tmp/_measure.pdf", format="A4", print_background=True)
        b.close()

    print(f"{'px':>6}  {'over':>4}  section")
    print("-" * 60)
    total = 0
    for title, h, w in secs:
        total += h
        flag = "WIDE" if w > width + 2 else ""
        print(f"{h:>6}  {flag:>4}  {title}")
    print("-" * 60)
    print(f"{total:>6}        TOTAL = {total / budget:.2f} pages of content")
    print(f"                (budget {budget}px per page at {width}px wide)")
    print("\nAny section flagged WIDE overflows its column and needs stacking.")
    return total


def sweep(path, zooms):
    """Find the largest zoom that still fits a page count."""
    import pypdfium2 as pdfium
    src = pathlib.Path(path)
    original = src.read_text()
    url = src.absolute().as_uri()
    try:
        with sync_playwright() as p:
            b = p.chromium.launch()
            for z in zooms:
                if re.search(r"body \{ zoom: [\d.]+; \}", original):
                    src.write_text(re.sub(r"body \{ zoom: [\d.]+; \}",
                                          f"body {{ zoom: {z}; }}", original))
                else:
                    src.write_text(original.replace(
                        "</style>", f"@media print {{ body {{ zoom: {z}; }} }}\n</style>"))
                pg = b.new_page()
                pg.goto(url)
                pg.wait_for_timeout(350)
                pg.pdf(path="/tmp/_sweep.pdf", format="A4", print_background=True)
                pg.close()
                n = len(pdfium.PdfDocument("/tmp/_sweep.pdf"))
                print(f"zoom {z:.2f} -> {n:>2} pages | {-(-n // 2):>2} sheets if printed 2-up "
                      f"| effective size x{z * 0.707:.2f} when 2-up")
            b.close()
    finally:
        src.write_text(original)
        print("\n(source restored; set the winning zoom yourself)")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("html")
    ap.add_argument("--width", type=int, default=703)
    ap.add_argument("--budget", type=int, default=1047)
    ap.add_argument("--sweep", type=float, nargs="+")
    a = ap.parse_args()
    if a.sweep:
        sweep(a.html, a.sweep)
    else:
        measure(a.html, a.width, a.budget)
