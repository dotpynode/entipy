from abc import ABC, abstractmethod
from .entity import Entity
from .component import Component

class System(ABC):
    @abstractmethod
    def update(self, entity : Entity,  components : list[Component]):
        pass 