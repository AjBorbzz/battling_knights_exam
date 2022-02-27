from dataclasses import dataclass, field
from operator import attrgetter

from combat import Combat
from position import Position


class Arena:

    def __init__(self):
        self.board = [tuple([Position(x,y) for y in range(0,8)]) for x in range(0,8)]

    def move_knight(self, knight, direction):
        knight.position.knight = None

        try:
            _position = self._direction_to_position(direction, knight.position)


        except Drowned:
            loot, last_position = Combat.kill_knight(knight, status=2)
            print(f"Your knight: {knight} is drowned")
            if self.drop_loot(loot, last_position):
                print(f"Dropped item: {loot}.")
        else:
            if self._is_square_with_knight(_position):
                # To Battle!
                winner, loser = Combat.attack(knight, _position.knight)
                self._move_knight_position(winner, _position)
                loot, last_position = Combat.kill_knight(loser)
                print(' -==Battle!!!==- ')
                print(' **Winner:', winner)
                print(' **Loser:', loser)
                if self.drop_loot(loot, last_position):
                    print(' Loot dropped:', loot)
                return winner

            if self._is_empty_square(_position):
                self._move_knight_position(knight, _position)
                print(' Moved', knight)
            elif self._is_square_with_item(_position):
                self._move_knight_position(knight, _position)
                _position.items.sort(key=attrgetter('priority'))
                if not knight.equipped:
                    knight.equipped = _position.items.pop()
                    print(' Acquired', knight.equipped)

            return knight




    def drop_loot(self, item, position):
        if item:
            item.position = position
            position.items.append(item)
            position.items.sort(key=attrgetter('priority'))
            return True

    def _move_knight_position(self, knight, position):
        knight.position = position
        position.knight = knight
        if knight.equipped:
            knight.equipped.position = position


    def render(self):
        print("")
        for row in self.board:
            for position in row:
                if position.knight:
                    print(f"{position.knight.id}",end='')
                elif len(position.items):
                    print(position.items[0].name[0] if position.items[0] else '', end='')
                else:
                    print('')
            print('')
        print('')

    def _direction_to_position(self, direction: str, old_position: Position):
        dir_map = {
            'N': (old_position.x-1, old_position.y),
            'W': (old_position.x, old_position.y-1),
            'E': (old_position.x, old_position.y+1),
            'S': (old_position.x+1, old_position.y),
        }

        x,y = dir_map[direction]

        if x < 0 or x > 7 or y < 0 or y > 7:
            raise Drowned('Knight Drowned')

        return self.board[x][y]

    def _is_empty_square(self, position):
        return not position.knight and len(position.items) == 0


    def _is_square_with_item(self, position):
        return len(position.items) > 0

    def _is_square_with_knight(self, position):
        return position.knight is not None


class Drowned(Exception):
    pass