# Jimmy

## Usage:

```python
from dispatcher.base import BaseDispatcher
from handlers.test_handler import TestHandler
from sensor_types.base import BaseSensorType

# create dispatcher
# you can have as many dispatchers as you want with unique handlers per each
dispatcher = BaseDispatcher()

# register some handlers
# there are two way to do it:
# first:
dispatcher.register(TestHandler())
# second:
dispatcher.register(TestHandler(), name="whatever", condition=callable(<handler>, <event>))

# for the first case handler shoud look like:

class TestHandler(BaseHandler):
    name = "TestName"

    def pre_load(self, event):
        print(f"Handler pre load: {event}")

    def post_load(self, event):
        print(f"Handler post load: {event}")

    def handle(self, event):
        print(f"Handler handle: {event}")

    def condition(self, event):
        return event.metadata["value"] > 9
# for the second one name and condition not required for the handler (because it passed directly to .register)

# now you should create an event
test_event = BaseSensorType(name="Test", metadata={"value": 10})
# event will be passed to dispatcher with the same name or in condition returns True for event

dispatcher.dispatch(test_event)

```
