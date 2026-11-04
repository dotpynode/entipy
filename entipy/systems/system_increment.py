from ..pattern.entity import Entity
from ..pattern.component import Component
from ..pattern.system import System
from ..components.component_counter import ComponentCounter
from ..utilities.utilities import Utilities

class SystemIncrement(System):
    def update(self, entity : Entity,  components : list[Component]):
        component = Utilities.try_get_component(components, ComponentCounter)
        if component is not None:
            component.cnt += 1
            #print(f'Entity: {entity.id} Counter {component.cnt}')