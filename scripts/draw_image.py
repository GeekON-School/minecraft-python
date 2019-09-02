import math
from collections import Counter

import mcpi.block as block
from PIL import Image
from mcpi.minecraft import Minecraft

y = 70
x = 0
z = 0

mc = Minecraft.create()
img = Image.open("../assets/lampas.jpg")
pixels = img.load()

wool_colors = [
    (228, 228, 228),  # white
    (234, 126, 53),  # orange
    (190, 73, 201),  # magenta
    (99, 135, 210),  # light blue
    (194, 181, 28),  # yellow
    (57, 186, 46),  # lime
    (217, 129, 153),  # pink
    (65, 65, 65),  # grey
    (160, 167, 167),  # light grey
    (38, 113, 145),  # cyan
    (126, 52, 191),  # purple
    (37, 49, 147),  # blue
    (86, 51, 28),  # brown
    (54, 75, 24),  # green
    (158, 43, 39),  # red
    (24, 20, 20)  # black
]


def d(a, b):
    return math.sqrt(sum((u - v) * (u - v) for u, v in zip(a, b)))


types = list(range(len(wool_colors)))
wool_counter = Counter()
for i in range(img.width):
    for j in range(img.height):
        color = pixels[i, j]
        wool_type = min(types, key=lambda k: d(wool_colors[k], color))
        wool_counter[wool_type] += 1
        mc.setBlock(x + i, y, z + j, block.Block(35, wool_type))

print(wool_counter)
