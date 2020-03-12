from collections import namedtuple

from sensor_types.base import BaseSensorType

handler_object = namedtuple("Handler", ("name", "condition", "handler"))


class BaseDispatcher:

    def __init__(self):
        self.handlers = []

    def register(self, handler, name=None, condition=None):
        name = name or getattr(handler, "name", None)
        condition = condition or getattr(handler, "condition", None)
        if not name and not condition:
            raise ValueError("You should provide valid name or condition.")
        self.handlers.append(handler_object(name, condition, handler))

    def dispatch(self, event: BaseSensorType):
        self.pre_load(event)
        for handler_obj in self.handlers:
            if event.validate(handler_obj):
                handler_obj.handler.pre_load(event)
                handler_obj.handler.handle(event)
                handler_obj.handler.post_load(event)
        self.post_load(event)

    def pre_load(self, event: BaseSensorType):
        pass

    def post_load(self, event: BaseSensorType):
        pass
