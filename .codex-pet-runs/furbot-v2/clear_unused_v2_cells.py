from pathlib import Path
from PIL import Image

root = Path('/Users/daltonreis/GitHub/dalton-reis/.codex-pet-runs/furbot-v2/final')
png = root / 'spritesheet-extended.png'
webp = root / 'spritesheet-extended.webp'
counts = [7, 8, 8, 4, 5, 8, 6, 6, 6, 8, 8]
cell_w, cell_h = 192, 208
im = Image.open(png).convert('RGBA')
for row, count in enumerate(counts):
    for col in range(count, 8):
        im.paste((0, 0, 0, 0), (col * cell_w, row * cell_h, (col + 1) * cell_w, (row + 1) * cell_h))
im.save(png)
im.save(webp, 'WEBP', lossless=True, method=6)
