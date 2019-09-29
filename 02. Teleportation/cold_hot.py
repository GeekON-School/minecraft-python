import random
import time

from mcpi.minecraft import Minecraft
from mcpi.vec3 import Vec3

mc = Minecraft.create()
my_id = mc.getPlayerEntityId('_Egor_S_')

rand_pos = Vec3(random.randint(-30, 30), 0, random.randint(-30, 30)) + mc.entity.getPos(my_id)
while True:
    shift = rand_pos - mc.entity.getPos(my_id)
    d = shift.length()
    if d < 1:
        mc.postToChat("You found it! Good job.")
        break
    mc.postToChat("Distance to target: {:2f}".format(d))
    time.sleep(1)
