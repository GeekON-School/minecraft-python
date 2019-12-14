from mcpi.block import *
from mcpi.minecraft import Minecraft
from mcpi.vec3 import Vec3


def range_blocks(a, b):
    for y in range(min(a.y, b.y), max(a.y, b.y) + 1):
        for x in range(min(a.x, b.x), max(a.x, b.x) + 1):
            for z in range(min(a.z, b.z), max(a.z, b.z) + 1):
                yield Vec3(x, y, z)


def main():
    whitelist = [DIAMOND_ORE.id, GOLD_ORE.id, LAPIS_LAZULI_ORE.id, IRON_ORE.id,
                 COAL_ORE.id, REDSTONE_ORE.id, BEDROCK.id]
    dy = 4
    dx = 16
    dz = 16

    mc = Minecraft.create()
    my_id = mc.getPlayerEntityId("_Egor_S_")
    pos = mc.entity.getTilePos(my_id)

    a = pos - Vec3(dx, dy, dz)
    a.y = max(0, a.y)
    b = pos + Vec3(dx, dy, dz)
    b.y = min(256, b.y)

    n = 0
    for bid, p in zip(mc.getBlocks(a, b), range_blocks(a, b)):
        if bid not in whitelist:
            mc.setBlock(p, AIR)
            n += 1
    mc.postToChat("{} blocks replaced".format(n))


if __name__ == '__main__':
    main()
