from dataclasses import dataclass

@dataclass
class Entity:
    def __init__(self, id : int):
        self.id : int = id

    def __eq__(self, other):
        if not isinstance(other, Entity):
            return NotImplemented
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)
    id : int