import random

from mcpi import block
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

x = random.randint(-32, 32)
y = 66
z = random.randint(-32, 32)

mc.postToChat("Go to ({}, {}, {})".format(x, y, z))
me = mc.getPlayerEntityId("_Egor_S_")
mc.entity.setPos(me, [x, y + 1, z])
mc.setBlock(x, y, z, block.GLASS.id)
