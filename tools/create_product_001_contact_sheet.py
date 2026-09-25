from pathlib import Path
from PIL import Image, ImageOps, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "products/001-caffeinated-slightly-overbooked/generated"
OUT = SRC / "PRODUCT-001-CONTACT-SHEET.png"

files = sorted(SRC.glob("*.png"))
assert len(files) == 20, f"Expected 20 PNGs, found {len(files)}"

thumb_w, thumb_h = 360, 432
label_h = 52
cols, rows = 4, 5
sheet = Image.new("RGB", (cols * thumb_w, rows * (thumb_h + label_h)), "white")
draw = ImageDraw.Draw(sheet)

for i, path in enumerate(files):
    with Image.open(path).convert("RGBA") as im:
        thumb = ImageOps.contain(im, (thumb_w - 24, thumb_h - 24))
        x = (i % cols) * thumb_w + (thumb_w - thumb.width) // 2
        y = (i // cols) * (thumb_h + label_h) + (thumb_h - thumb.height) // 2
        sheet.paste(Image.new("RGB", thumb.size, "white"), (x, y))
        sheet.paste(thumb, (x, y), thumb)
    label = path.stem.replace("-4500x5400", "")
    draw.text(((i % cols) * thumb_w + 12, (i // cols) * (thumb_h + label_h) + thumb_h + 12), label, fill="black")

sheet.save(OUT, "PNG")
print(f"PASS: created visual contact sheet {OUT}")
