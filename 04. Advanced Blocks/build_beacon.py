from mcpi.block import *
from mcpi.minecraft import Minecraft
from mcpi.vec3 import Vec3

mc = Minecraft.create()
my_id = mc.getPlayerEntityId("_Egor_S_")

center = mc.entity.getTilePos(my_id) - Vec3(0, 1, 0)
height = 6

mc.setBlock(center, 138)
for y in range(1, height + 1):
    mc.setBlocks(center + Vec3(-y, -y, -y), center + Vec3(y, -y, y), IRON_BLOCK)
