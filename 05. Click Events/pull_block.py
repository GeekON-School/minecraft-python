import time

from mcpi.block import *
from mcpi.minecraft import Minecraft
from mcpi.vec3 import Vec3

mc = Minecraft.create()

# SWORD ONLY!
# +x: 5
# -x: 4
# +y: 1
# -y: 0
# +z: 3
# -z: 2

while True:
    for ev in mc.events.pollBlockHits():
        if mc.getBlock(ev.pos) != BEDROCK.id:
            continue
        mc.setBlock(ev.pos, AIR)
        if ev.face == 4:
            mc.setBlock(ev.pos + Vec3(-1, 0, 0), BEDROCK)
        elif ev.face == 5:
            mc.setBlock(ev.pos + Vec3(1, 0, 0), BEDROCK)
        elif ev.face == 3:
            mc.setBlock(ev.pos + Vec3(0, 0, 1), BEDROCK)
        elif ev.face == 2:
            mc.setBlock(ev.pos + Vec3(0, 0, -1), BEDROCK)

    time.sleep(1)
