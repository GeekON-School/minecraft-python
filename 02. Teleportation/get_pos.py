from mcpi.minecraft import Minecraft

mc = Minecraft.create()
my_id = mc.getPlayerEntityId('_Egor_S_')
pos = mc.entity.getPos(my_id)
tile_pos = mc.entity.getTilePos(my_id)
print(pos - tile_pos)
