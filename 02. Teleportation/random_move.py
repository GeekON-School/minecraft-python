import random

from mcpi.minecraft import Minecraft
from mcpi.vec3 import Vec3

mc = Minecraft.create()
my_id = mc.getPlayerEntityId('_Egor_S_')

shift = Vec3(random.randint(-30, 30), random.randint(-30, 30), random.randint(-30, 30))
pos = mc.entity.getPos(my_id) + shift
mc.entity.setPos(my_id, pos)
mc.postToChat("Poof! It's magic!")
