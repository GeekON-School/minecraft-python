from mcpi.block import *
from mcpi.minecraft import Minecraft
from mcpi.vec3 import Vec3

mc = Minecraft.create()


def small_house(start_pos):
    mc.setBlocks(start_pos, start_pos + Vec3(7, 0, 5), BRICK_BLOCK)  # bottom
    mc.setBlocks(start_pos + Vec3(0, 1, 0), start_pos + Vec3(7, 4, 0), WOOD_PLANKS)  # left wall
    mc.setBlocks(start_pos + Vec3(0, 1, 5), start_pos + Vec3(7, 4, 5), WOOD_PLANKS)  # right wall
    mc.setBlocks(start_pos + Vec3(0, 1, 1), start_pos + Vec3(0, 6, 4), WOOD_PLANKS)  # front wall
    mc.setBlocks(start_pos + Vec3(7, 1, 1), start_pos + Vec3(7, 6, 4), WOOD_PLANKS)  # back wall
    left_stairs = Block(STAIRS_WOOD.id, 2)
    mc.setBlocks(start_pos + Vec3(-1, 4, -1), start_pos + Vec3(8, 4, -1), left_stairs)
    mc.setBlocks(start_pos + Vec3(-1, 5, 0), start_pos + Vec3(8, 5, 0), left_stairs)
    mc.setBlocks(start_pos + Vec3(-1, 6, 1), start_pos + Vec3(8, 6, 1), left_stairs)
    mc.setBlocks(start_pos + Vec3(-1, 7, 2), start_pos + Vec3(8, 7, 2), left_stairs)
    right_stairs = Block(STAIRS_WOOD.id, 3)
    mc.setBlocks(start_pos + Vec3(-1, 4, 6), start_pos + Vec3(8, 4, 6), right_stairs)
    mc.setBlocks(start_pos + Vec3(-1, 5, 5), start_pos + Vec3(8, 5, 5), right_stairs)
    mc.setBlocks(start_pos + Vec3(-1, 6, 4), start_pos + Vec3(8, 6, 4), right_stairs)
    mc.setBlocks(start_pos + Vec3(-1, 7, 3), start_pos + Vec3(8, 7, 3), right_stairs)
    # doors
    mc.setBlocks(start_pos + Vec3(0, 1, 2), start_pos + Vec3(0, 2, 3), AIR)
    # windows
    mc.setBlocks(start_pos + Vec3(3, 2, 0), start_pos + Vec3(4, 3, 0), GLASS)
    mc.setBlocks(start_pos + Vec3(3, 2, 5), start_pos + Vec3(4, 3, 5), GLASS)
    mc.setBlocks(start_pos + Vec3(7, 2, 2), start_pos + Vec3(7, 3, 3), GLASS)


for z in range(-90, 200, 12):
    small_house(Vec3(340, 134, z))
