from mcpi.block import *
from mcpi.minecraft import Minecraft
from mcpi.vec3 import Vec3

mc = Minecraft.create()
my_id = mc.getPlayerEntityId("_Egor_S_")

center = mc.entity.getTilePos(my_id) - Vec3(0, 1, 0)
radius = 10
for x in range(center.x - radius, center.x + radius + 1):
    for y in range(center.y - radius, center.y + radius + 1):
        for z in range(center.z - radius, center.z + radius + 1):
            pos = Vec3(x, y, z)
            if radius - 0.5 <= (pos - center).length() <= radius + 0.5:
                mc.setBlock(pos, GLASS)
