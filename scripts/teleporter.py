import time

from mcpi.minecraft import Minecraft
from mcpi.vec3 import Vec3

mc = Minecraft.create()

# Portal location
pos_in = Vec3(222, -9, -68)
pos_out = Vec3(222, 6, -39)

while True:
    for player in mc.getPlayerEntityIds():
        pos = mc.entity.getTilePos(player)
        if pos_in.x - 1 <= pos.x <= pos_in.x + 1:
            if pos_in.y - 1 <= pos.y <= pos_in.y + 1:
                if pos_in.z - 1 <= pos.z <= pos_in.z + 1:
                    mc.postToChat("We need to go deeper!")
                    mc.entity.setTilePos(player, pos_out)
    time.sleep(2)
