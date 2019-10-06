from mcpi.block import *
from mcpi.minecraft import Minecraft
from mcpi.vec3 import Vec3

mc = Minecraft.create()

my_pos = Vec3(0, 64, 0)  # координаты синей шерсти
blue_wool = Block(WOOL.id, 11)
mc.setBlock(my_pos, blue_wool)

block = mc.getBlock(my_pos)
block_with_data = mc.getBlockWithData(my_pos)

print(block, blue_wool.id == block)  # 35 True
print(block_with_data, blue_wool.id == block_with_data.id,
      blue_wool.data == block_with_data.data)  # Block(35, 11) True True
