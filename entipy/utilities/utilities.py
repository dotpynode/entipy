from ..pattern.component import Component
from typing import TypeVar

T = TypeVar("T", bound=Component)

class Utilities:
    @staticmethod
    def try_get_component(components: list[Component], component_type: type[T]) -> T | None:
        return next((c for c in components if isinstance(c, component_type)), None)