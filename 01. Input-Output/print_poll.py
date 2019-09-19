import time

from mcpi.minecraft import Minecraft

mc = Minecraft.create()

while True:
    for msg in mc.events.pollChatPosts():
        print(msg.entityId, msg.message)
    time.sleep(3)
