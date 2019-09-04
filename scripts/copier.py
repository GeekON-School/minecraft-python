from mcpi.minecraft import Minecraft
from mcpi.vec3 import Vec3

mc = Minecraft.create()

pos_1 = Vec3(257, -9, -52)
pos_2 = Vec3(259, -5, -48)

pos_new = Vec3(267, 0, -42)

for x in range(pos_2.x - pos_1.x + 1):
    for y in range(pos_2.y - pos_1.y + 1):
        for z in range(pos_2.z - pos_1.z + 1):
            shift = Vec3(x, y, z)
            block = mc.getBlockWithData(pos_1 + shift)
            mc.setBlock(pos_new + shift, block)
