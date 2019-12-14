from PIL import Image
from mcpi.minecraft import Minecraft
from mcpi.vec3 import Vec3
from mcpi.block import *


def range_blocks(a, b):
    for y in range(min(a.y, b.y), max(a.y, b.y) + 1):
        for x in range(min(a.x, b.x), max(a.x, b.x) + 1):
            for z in range(min(a.z, b.z), max(a.z, b.z) + 1):
                yield Vec3(x, y, z)


def main():
    diamond = (0, 190, 250)
    gold = (250, 250, 0)
    redstone = (250, 0, 0)
    dy = 2
    dx = 32
    dz = 32

    mc = Minecraft.create()
    my_id = mc.getPlayerEntityId("_Egor_S_")
    pos = mc.entity.getTilePos(my_id)

    a = pos - Vec3(dx, dy, dz)
    a.y = max(0, a.y)
    b = pos + Vec3(dx, dy, dz)
    b.y = min(256, b.y)

    img = Image.new("RGB", (b.x - a.x + 1, b.z - a.z + 1))

    for bid, p in zip(mc.getBlocks(a, b), range_blocks(a, b)):
        ip = (p.x - a.x, p.z - a.z)
        if bid == DIAMOND_ORE.id:
            img.putpixel(ip, diamond)
        if bid == GOLD_ORE.id and img.getpixel(ip) not in [diamond]:
            img.putpixel(ip, gold)
        if bid == REDSTONE_ORE.id and img.getpixel(ip) not in [diamond, gold]:
            img.putpixel(ip, redstone)

    img.save("diamonds_map.png")


if __name__ == '__main__':
    main()
