from pathlib import Path
import xml.etree.ElementTree as ET
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
PRODUCT = ROOT / "products/001-caffeinated-slightly-overbooked"
masters = [PRODUCT / "MASTER.svg"] + sorted((PRODUCT / "designs").glob("*.svg"))

assert len(masters) == 20, f"Expected 20 SVG masters, found {len(masters)}"

for src in masters:
    root = ET.parse(src).getroot()
    assert root.tag.endswith("svg"), src
    assert root.attrib.get("width") == "4500", src
    assert root.attrib.get("height") == "5400", src
    assert root.attrib.get("viewBox") == "0 0 4500 5400", src

    if src.name == "MASTER.svg":
        png = PRODUCT / "generated/01-caffeinated-slightly-overbooked-4500x5400.png"
    else:
        png = PRODUCT / "generated" / f"{src.stem}-4500x5400.png"

    assert png.exists(), f"Missing PNG: {png}"
    with Image.open(png) as im:
        assert im.size == (4500, 5400), (png, im.size)
        assert im.mode in ("RGBA", "LA"), (png, im.mode)
        assert im.getchannel("A").getextrema()[0] == 0, f"PNG is not transparent: {png}"

print("PASS: all 20 SVG masters and 20 transparent 4500x5400 PNG assets validated.")
