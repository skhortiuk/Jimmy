from sensor_types.base import BaseSensorType


class BaseHandler:
    name: str = None

    def pre_load(self, event: BaseSensorType):
        pass

    def post_load(self, event: BaseSensorType):
        pass

    def handle(self, event: BaseSensorType):
        pass

    def condition(self, event: BaseSensorType) -> bool:
        pass
