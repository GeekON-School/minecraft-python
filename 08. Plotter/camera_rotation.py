from mcpi.minecraft import Minecraft


def main():
    mc = Minecraft.create()
    my_id = mc.getPlayerEntityId("_Egor_S_")
    mc.entity.getRotation(my_id)


if __name__ == '__main__':
    main()
