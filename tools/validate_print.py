from pathlib import Path
import re
import xml.etree.ElementTree as ET
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
PRODUCT = ROOT / "products/001-caffeinated-slightly-overbooked"
SVG = PRODUCT / "MASTER.svg"
PNG = PRODUCT / "generated/PRODUCT-001-4500x5400.png"

root = ET.parse(SVG).getroot()
assert root.tag.endswith("svg")
assert root.attrib.get("width") == "4500"
assert root.attrib.get("height") == "5400"
assert root.attrib.get("viewBox") == "0 0 4500 5400"

svg_text = SVG.read_text(encoding="utf-8")
assert not re.search(r'<rect[^>]+(?:fill=["\'](?:white|#fff(?:fff)?)["\'])', svg_text, re.I)
assert "Caffeinated &amp; Slightly Overbooked" in svg_text
assert "OVERBOOKED" in svg_text

with Image.open(PNG) as im:
    assert im.size == (4500, 5400), im.size
    assert im.mode in ("RGBA", "LA"), im.mode
    alpha = im.getchannel("A")
    assert alpha.getextrema()[0] == 0, "PNG must retain transparent background"

print("PASS: SVG structure, canvas, content and PNG transparency/dimensions are valid.")
