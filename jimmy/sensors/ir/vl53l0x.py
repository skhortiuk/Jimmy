import logging

from vl53l0x import VL53L0X

from jimmy.sensors.base import BaseSensor


class VL53L0XSensor(VL53L0X, BaseSensor):
    logger = logging.getLogger()

    def get_data(self) -> int:
        data = super(VL53L0XSensor, self).get_data()
        logging.info(f'[*] Calling get data from {self}')
        return data
