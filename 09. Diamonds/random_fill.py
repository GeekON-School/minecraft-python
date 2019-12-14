import time
import random
from mcpi.block import *
from mcpi.minecraft import Minecraft
from mcpi.vec3 import Vec3


def range_blocks(a, b):
    for y in range(min(a.y, b.y), max(a.y, b.y) + 1):
        for x in range(min(a.x, b.x), max(a.x, b.x) + 1):
            for z in range(min(a.z, b.z), max(a.z, b.z) + 1):
                yield Vec3(x, y, z)


def main():
    bid = WOOL.id
    r = 8

    mc = Minecraft.create()
    my_id = mc.getPlayerEntityId("_Egor_S_")
    pos = mc.entity.getTilePos(my_id) + Vec3(0, 16, 0)

    a = pos - Vec3(r, r, r)
    a.y = max(0, a.y)
    b = pos + Vec3(r, r, r)
    b.y = min(256, b.y)

    cube = list(range_blocks(a, b))
    while True:
        mc.setBlock(random.choice(cube), Block(bid, random.randint(0, 15)))
        time.sleep(0.5)


if __name__ == '__main__':
    main()
