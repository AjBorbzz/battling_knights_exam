from dataclasses import dataclass
from position import Position

@dataclass
class Item:
    name: str
    priority: int
    position: Position
    attack: int
    defense: int