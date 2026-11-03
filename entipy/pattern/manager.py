from .entity import Entity
from .component import Component

class Manager:
    def __init__(self) -> None:
        self.m_EC : dict[Entity, list[Component]] = {}

    def add_entity(self, entity : Entity) -> None:
        if not isinstance(entity, Entity):
            raise ValueError(f'Entity must be type of {str(Entity)}.')
        if entity in self.m_EC:
            raise ValueError(f'Entity with id {entity.id} already exists.')
        self.m_EC[entity] = []
    
    def remove_entity(self, entity : Entity) -> None:
        if not isinstance(entity, Entity):
            raise ValueError(f'Entity must be type of {str(Entity)}.')
        if entity not in self.m_EC:
            raise ValueError(f'Entity with id {entity.id} does not exists.')
        self.m_EC.pop(entity)

    def add_component(self, entity : Entity, component : Component) -> None:
        if not isinstance(entity, Entity):
            raise ValueError(f'Entity must be type of {str(Entity)}.')
        if not isinstance(component, Component):
            raise ValueError(f'Component must be type of {str(Component)}.')
        if entity not in self.m_EC:
            raise ValueError(f'Entity with id {entity.id} does not exists.')
        if component in self.m_EC[entity]:
            raise ValueError(f'Component is already assigned to entity.')
        self.m_EC[entity].append(component)

    def remove_component(self, entity : Entity, componenet : Component) -> None:
        pass