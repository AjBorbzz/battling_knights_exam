from arena import Arena
from item import Item
from knight import Knight
from serialize import Serialize

class GameStart:
    def setup_board(self):
        self.arena = Arena()
        arena_board = self.arena.board

        self.R = Knight('R', 'red', arena_board[0][0])
        self.Y = Knight('Y', 'yellow', arena_board[0][7])
        self.B = Knight('B', 'blue', arena_board[7][0])
        self.G = Knight('G', 'green', arena_board[7][7])

        arena_board[0][0].knight = self.R
        arena_board[0][7].knight = self.Y
        arena_board[7][0].knight = self.B
        arena_board[7][7].knight = self.G

        self.item_axe = Item('Axe', 4, arena_board[2][2], 2, 0)
        self.item_dagger = Item('Dagger', 2, arena_board[2][5], 1, 0)
        self.item_magicstaff = Item('MagicStaff', 3, arena_board[5][2], 1, 1)
        self.item_helmet = Item('Helmet', 1, arena_board[5][5], 0, 1)

        arena_board[2][2].items.append(self.item_axe)
        arena_board[2][5].items.append(self.item_dagger)
        arena_board[5][2].items.append(self.item_magicstaff)
        arena_board[5][5].items.append(self.item_helmet)

        return (
            self.arena,
            self.R,
            self.Y,
            self.B,
            self.G,
            self.item_axe,
            self.item_dagger,
            self.item_magicstaff,
            self.item_helmet,
        )

    def run_instructions(self):
        instructions = Serialize.read_moves()

        for (knight_id, direction) in instructions:
            knight = getattr(self, knight_id)
            self.arena.move_knight(knight, direction)
