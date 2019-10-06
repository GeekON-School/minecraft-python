import time

from mcpi.block import *
from mcpi.minecraft import Minecraft
from mcpi.vec3 import Vec3

mc = Minecraft.create()
gate_pos = Vec3(285, 134, 68)
key_pos = Vec3(287, 134, 69)
true_key = Block(WOOL.id, 10)

while True:
    block_to_place = BEDROCK
    key = mc.getBlockWithData(key_pos)
    if key == true_key:
        block_to_place = AIR
    mc.setBlock(gate_pos + Vec3(0, 0, 0), block_to_place)
    mc.setBlock(gate_pos + Vec3(1, 0, 0), block_to_place)
    mc.setBlock(gate_pos + Vec3(0, 1, 0), block_to_place)
    mc.setBlock(gate_pos + Vec3(1, 1, 0), block_to_place)
    time.sleep(1)
