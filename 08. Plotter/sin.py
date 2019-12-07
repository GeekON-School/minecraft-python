import random
from math import *

from mcpi.block import *
from mcpi.minecraft import Minecraft
from mcpi.vec3 import Vec3


def f(t):
    x = -10 + t / 10
    y = 10 * sin(t / 100)
    z = 5
    return Vec3(round(x), round(y), round(z))


def main():
    mc = Minecraft.create()
    my_id = mc.getPlayerEntityId("_Egor_S_")
    my_pos = mc.entity.getTilePos(my_id)

    for t in range(int(500 * pi * 2 + 1)):
        shift = f(t)
        mc.setBlock(my_pos + shift, Block(WOOL.id, random.randint(0, 15)))


if __name__ == '__main__':
    main()
