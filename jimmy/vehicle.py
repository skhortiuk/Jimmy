from typing import Dict, Union
import logging

from jimmy.sensors.base import BaseSensor, SensorData
from jimmy.utils import millis
from jimmy.config import SECOND


class Vehicle:
    logger = logging.getLogger()

    def __init__(self):
        # Todo: Add modules validation (unique, isinstance(BaseModule),
        #  module loaded correctly)
        self._sensors: Dict[Union[str, BaseSensor]] = {}
        self._data: Dict[Union[str, SensorData]] = {}

    def control(self) -> None:
        """Do main control functions based on received data from sensors.
        """
        pass

    def attach_sensor(self, sensor: BaseSensor, name: str):
        self.logger.info(f'Trying to attach new sensor to vehicle. Name: {name}. Sensor: {sensor}')
        if not isinstance(sensor, BaseSensor):
            err_msg = f'Expected type of BaseSensor, instead of {type(sensor)}'
            self.logger.error(err_msg)
            raise TypeError(err_msg)

        self._sensors[name] = sensor
        self.logger.info(f'New sensor attached to vehicle. Name: {name}. Sensor: {sensor}')

    def get_sensor(self, name: str) -> BaseSensor:
        return self._sensors[name]

    def run(self, frequency: int = 50) -> None:
        """Main routine

        Args:
            frequency: Determines how often vehicle will be asked new data
                from sensors and call `self.control` function.
                0 - means call `self.control` when new data from sensors
                available.
        """
        wait_time = SECOND / frequency
        self.logger.info(f'Loop frequency = {frequency}.')
        tic = millis()
        self.logger.info(f'Founded {len(self._sensors)} sensors.')
        while True:
            if tic - millis() > wait_time:
                for name, module in self._sensors.items():
                    if module.data_ready is False:
                        self.logger.info(f'New data is not ready for sensor. Name: {name}. Module: {module}.')
                        continue

                    data = module.get_data()
                    self.logger.info(f'Received new data from sensor. Name: {name}. Data: {data}.')
                    self._data[name] = data

                self.control()

                tic = millis()
