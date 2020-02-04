from abc import ABCMeta, abstractmethod

from jimmy.utils import millis

from jimmy.config import SECOND


class SensorData:
    pass


class BaseSensor(metaclass=ABCMeta):
    def __init__(self, update_frequency: int = 50):
        self._frequency = update_frequency
        self._update_time: int = SECOND // self._frequency
        self._sensor_enabled: bool = False
        self._tic: float = millis()

    @property
    def data_ready(self):
        return millis() - self._tic > self._update_time

    @property
    def update_frequency(self):
        return self._frequency

    @update_frequency.setter
    def update_frequency(self, value: int):
        if not isinstance(value, int):
            raise TypeError(f"Expected `frequency` type is int, not {type(value)}")
        if value < 0:
            raise ValueError(f"Expected `frequency` greater than 0, not {value}")

        self._frequency = value
        self._update_time = SECOND // self._frequency

    @abstractmethod
    def get_data(self) -> SensorData:
        pass
