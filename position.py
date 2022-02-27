from dataclasses import dataclass, field

@dataclass
class Position:
    x: int
    y: int

    knight: dict = None
    items: list = field(default_factory=list)

    def __repr__(self):
        return f'[{self.x} , {self.y} ]'

    def to_json(self):
        return [self.x, self.y]
        