from pathlib import Path
import cairosvg

ROOT = Path(__file__).resolve().parents[1]
src = ROOT / "products/001-caffeinated-slightly-overbooked/MASTER.svg"
out = ROOT / "products/001-caffeinated-slightly-overbooked/generated/PRODUCT-001-4500x5400.png"
out.parent.mkdir(parents=True, exist_ok=True)

cairosvg.svg2png(
    url=str(src),
    write_to=str(out),
    output_width=4500,
    output_height=5400,
)
print(f"Generated {out} at 4500x5400 RGBA.")
