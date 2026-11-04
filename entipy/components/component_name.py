from ..pattern.component import Component
from dataclasses import dataclass

@dataclass
class ComponentName(Component):
    name : str = ""

    def __init__(self, name : str):
        self.name = name