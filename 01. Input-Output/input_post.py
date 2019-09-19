import time

from mcpi.minecraft import Minecraft

mc = Minecraft.create()

while True:
    s = input()
    mc.postToChat("<Python> " + s)
    time.sleep(1)
