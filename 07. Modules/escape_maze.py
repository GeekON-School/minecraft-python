import random
import time

from maze import generate_maze
from mcpi.block import *
from mcpi.minecraft import Minecraft
from mcpi.vec3 import Vec3

maze_pos = Vec3(0, 100, 0)
width = 35
height = 35

mc = Minecraft.create()
my_id = mc.getPlayerEntityId('_Egor_S_')
m = generate_maze(width, height)

for i, row in enumerate(m):
    for j, mb in enumerate(row):
        if mb == 1:
            floor_block = WOOD
            wall_block = LEAVES
        else:
            floor_block = GLOWSTONE_BLOCK
            wall_block = AIR
        mc.setBlock(maze_pos + Vec3(i, 0, j), floor_block)
        mc.setBlocks(maze_pos + Vec3(i, 1, j), maze_pos + Vec3(i, 4, j), wall_block)

start_pos = maze_pos + Vec3(2 * random.randint(0, height // 2) + 1, 1, 2 * random.randint(0, width // 2) + 1)
end_pos = maze_pos + Vec3(2 * random.randint(0, height // 2) + 1, 1, 2 * random.randint(0, width // 2) + 1)

mc.entity.setTilePos(my_id, start_pos)
mc.setBlock(end_pos + Vec3(0, -1, 0), Block(GLASS.id, 14))
mc.setBlock(end_pos + Vec3(0, -2, 0), 138)
mc.setBlocks(end_pos + Vec3(-1, -3, -1), end_pos + Vec3(1, -3, 1), IRON_BLOCK)

start_time = time.monotonic()
while True:
    pos = mc.entity.getTilePos(my_id)
    if (pos - end_pos).length() < 1.5:
        break
    if mc.getBlock(pos + Vec3(0, -1, 0)) == GLOWSTONE_BLOCK.id:
        mc.setBlock(pos + Vec3(0, -1, 0), OBSIDIAN)
    time.sleep(0.3)

end_time = time.monotonic()
mc.postToChat("You did it! Your time: {:.02f}".format(end_time - start_time))
