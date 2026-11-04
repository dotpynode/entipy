from ..pattern.component import Component
from dataclasses import dataclass

@dataclass
class ComponentCounter(Component):
    cnt : int = 0