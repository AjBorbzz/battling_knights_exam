# Battling Knights

Note: This requires `Python 3.7` to run since it leverages the new `@dataclass` notation.
Requirements: 
at least `Python 3.7`.

Python Classes:

The `Arena` this class will initialize the board, knights' positions and items' positions.

The `Knight` class properties are: ID, position, item equipped, base attack, etc.

The `Item` class to describe items on the board.

The `Position` class is used by Knight, Item and Arena to determine their position.

A `Combat` class which deals with the life and death of knights.

A `Serialize` class to read and write to the FS.

A `GameStart` class which brings everything together:

- reads instructions
- sets initial knight positions
- runs the game


These classes reference each other like so:

- A knight instance has a `position` attribute so it always knows where it's placed on the board.
- A `position` instance always knows whether it holds _items_ or a _knight_.
- An `item` instance will always reference its position as well.

We are able to determine the position of a knight either by referring to `knight.position`
or by referring to `arena.board`.


# Outline of classes

## Knight class:

    ID: R
    position: <Position>
    equipped: <Item>
    BaseAttack: 1
    BaseDefense: 1

## Arena class:

**Properties**

    board - 2 dimensional matrix
            each item is a Position element

**Methods**

    move_knight - allowed (N,S,E,W)
        move_empty_square - update position
        move_square_with_loot - equip item, according to (A,M,D,H) rule
        move_square_with_knight - attack
        move_square_with_water - drown, drop items

## Position class:

    position: (0, 0)
    knight_ids: ()
    item_ids: ()

## Serialize class:

- Read instructions from from the `moves.txt` file
- Serialize to JSON format and write to FS.


## Combat class:

    Combat and kill knights.


## GameStart class:

    Run instructions and update Arena, Knights, etc.


# Usage

To run the app:

    python run.py


Moves are read in from `moves.txt`.

The output is written to `final_state.json`.
