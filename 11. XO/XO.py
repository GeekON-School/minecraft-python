import time

from mcpi.block import *
from mcpi.minecraft import Minecraft
from mcpi.vec3 import Vec3


class TicTacToe:
    def __init__(self, mc, corners, win=4):
        self.mc = mc
        self.corners = corners
        self.win = win
        self.series_len = 0
        self.series_block = None
        self.player = ("Gold", GOLD_BLOCK.id)
        self.second_player = ("Diamond", DIAMOND_BLOCK.id)
    
    def build_field(self):
        self.mc.setBlocks(self.corners[0] - Vec3(2, 4, 2), self.corners[1] + Vec3(2, 7, 2), AIR)
        self.mc.setBlocks(self.corners[0] - Vec3(1, 1, 1), self.corners[1] + Vec3(1, 0, 1), BEDROCK)
        self.mc.setBlocks(self.corners[0], self.corners[1], WOOL)

    def get_field(self):
        field = []
        width = self.corners[1].x - self.corners[0].x + 1
        for i, block in enumerate(self.mc.getBlocks(self.corners[0], self.corners[1])):
            if i % width == 0:
                field.append([])
            field[-1].append(block)
        return field

    def _update_series(self, block):
        if block == self.series_block:
            self.series_len += 1
        elif block in [self.player[1], self.second_player[1]]:
            self.series_block = block
            self.series_len = 1
        else:
            self._reset_series()

    def _reset_series(self):
        self.series_block = None
        self.series_len = 0

    def _get_winner(self):
        assert self.series_len >= self.win
        if self.series_block == self.player[1]:
            return self.player
        else:
            return self.second_player

    def check_winner(self):
        self._reset_series()
        field = self.get_field()
        # horizontal & vertical
        for m in [field, list(zip(*field))]:
            for line in m:
                for block in line:
                    self._update_series(block)
                    if self.series_len >= self.win:
                        return self._get_winner()
                self._reset_series()
        # diagonals
        for m in [field, field[::-1]]:
            for y in range(len(m) - self.win):
                for t in range(min(len(m[0]), len(m) - y)):
                    self._update_series(m[y + t][t])
                    if self.series_len >= self.win:
                        return self._get_winner()
                self._reset_series()
            for x in range(1, len(m[0]) - self.win):
                for t in range(min(len(m), len(m[0]) - x)):
                    self._update_series(m[t][x + t])
                    if self.series_len >= self.win:
                        return self._get_winner()
                self._reset_series()
        return None

    def done_step(self):
        self.player, self.second_player = self.second_player, self.player
        self.mc.postToChat("{} - it's your turn".format(self.player[0]))

    def handle_click(self, pos):
        if pos.y == self.corners[0].y and self.corners[0].x <= pos.x <= self.corners[1].x and self.corners[
            0].z <= pos.z <= self.corners[1].z:
            if self.mc.getBlock(pos) not in [self.player[1], self.second_player[1]]:
                self.mc.setBlock(pos, self.player[1])
                return True
            return False
        return None


def main():
    mc = Minecraft.create()
    bob_id = mc.getPlayerEntityId("_Egor_S_")
    pos = mc.entity.getTilePos(bob_id)
    corner_1 = pos + Vec3(0, -1, 0)
    corner_2 = pos + Vec3(15, -1, 15)

    ttt = TicTacToe(mc, (corner_1, corner_2))
    ttt.build_field()
    ttt.done_step()  # fake

    while True:
        cr = None
        for ev in mc.events.pollBlockHits():
            cr = ttt.handle_click(ev.pos)
            if cr is not None:
                break
        if cr is False:
            mc.postToChat("Wrong move! Choose another cell.")
        elif cr is True:
            wr = ttt.check_winner()
            if wr is not None:
                mc.postToChat("{} is winner!".format(wr[0]))
                break
            else:
                ttt.done_step()
        time.sleep(0.5)


if __name__ == '__main__':
    main()
