import time

from mcpi.block import *
from mcpi.minecraft import Minecraft

mc = Minecraft.create()
my_id = mc.getPlayerEntityId("_Egor_S_")
my_wool = Block(WOOL.id, 10)

while True:
    tile_pos = mc.entity.getTilePos(my_id)
    tile_pos.y -= 1
    mc.setBlock(tile_pos, my_wool)
    time.sleep(1)
