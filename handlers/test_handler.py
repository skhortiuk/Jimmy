from handlers.base import BaseHandler


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
