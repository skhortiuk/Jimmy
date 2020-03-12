from dataclasses import dataclass, field
from typing import AnyStr, Dict


@dataclass
class BaseSensorType:
    name: AnyStr = None
    metadata: Dict = field(repr=False, default_factory=dict)

    def validate(self, handler) -> bool:
        return self.name == handler.name or (handler.condition or (lambda e: False))(self) is True
