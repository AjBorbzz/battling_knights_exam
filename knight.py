import json
from dataclasses import dataclass, field
from item import Item
from position import Position

STATUS_OPTIONS = ['ALIVE', 'DEAD', 'DROWNED']

@dataclass
class Knight:
    id: str
    color: str
    position: Position
    status: str = STATUS_OPTIONS[0]
    equipped: Item = None
    base_attack: int= 1
    base_defense: int= 1

    def update_status(self, idx):
        self.status = STATUS_OPTIONS[idx]

