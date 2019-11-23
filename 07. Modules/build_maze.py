from maze import generate_maze
from mcpi.block import *
from mcpi.minecraft import Minecraft
from mcpi.vec3 import Vec3

maze_pos = Vec3(0, 100, 0)

mc = Minecraft.create()
m = generate_maze(35, 35)

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
