
from gamestart import GameStart
from serialize import Serialize

if __name__ == '__main__':
    game = GameStart()

    (
        arena,
        knight_R,
        knight_Y,
        knight_B,
        knight_G,
        item_axe,
        item_dagger,
        item_magicstaff,
        item_helmet,
    ) = game.setup_board()

    game.arena.render()

    game.run_instructions()

    game.arena.render()

    state = Serialize.serialize_gamestate((knight_R, knight_Y, knight_B, knight_G), (item_axe, item_dagger, item_magicstaff, item_helmet))
    Serialize.commit_to_fs(state)