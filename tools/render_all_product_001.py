from pathlib import Path
import cairosvg

ROOT = Path(__file__).resolve().parents[1]
PRODUCT = ROOT / "products/001-caffeinated-slightly-overbooked"
OUT = PRODUCT / "generated"
OUT.mkdir(parents=True, exist_ok=True)

# Remove stale generated PNGs so validation/contact-sheet counts only this run.
for stale in OUT.glob("*.png"):
    stale.unlink()

masters = [PRODUCT / "MASTER.svg"] + sorted((PRODUCT / "designs").glob("*.svg"))
count = 0

for src in masters:
    if src.name.endswith("-QA.svg"):
        continue
    if src.name == "MASTER.svg":
        filename = "01-caffeinated-slightly-overbooked-4500x5400.png"
    else:
        filename = f"{src.stem}-4500x5400.png"
    target = OUT / filename
    cairosvg.svg2png(
        url=str(src),
        write_to=str(target),
        output_width=4500,
        output_height=5400,
        background_color=None,
    )
    count += 1
    print(f"Generated {target}")

assert count == 20, f"Expected 20 masters, rendered {count}"
print(f"PASS: rendered {count} product masters at 4500x5400 transparent PNG.")
