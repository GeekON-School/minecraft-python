import time

from mcpi.minecraft import Minecraft

mc = Minecraft.create()

while True:
    for player in mc.getPlayerEntityIds():
        pos = mc.entity.getTilePos(player)
        print(player, pos)
    time.sleep(2)
