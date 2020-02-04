from jimmy.utils import millis
from jimmy.config import SECOND


class Vehicle:
    def __init__(self):
        # Todo: Add modules validation (unique, isinstance(BaseModule),
        #  module loaded correctly)
        self.sensors = {}
        self.data = {}

    def control(self) -> None:
        """Do main control functions based on data received from sensors.
        """
        pass

    def run(self, frequency: int = 50) -> None:
        """Main routine

        Args:
            frequency: Determines how often vehicle will be asked new data
                from sensors and call `self.control` function.
                0 - means call `self.control` when new data from sensors
                available.
        """
        # Todo: Make control only when new data received
        # Todo: Provide logger support (when config.LOGGING = True)
        wait_time = SECOND / frequency
        tic = millis()

        while True:
            if tic - millis() > wait_time:
                for name, module in self.sensors.items():
                    self.data[name] = module.get_data()

                self.control()

                tic = millis()
