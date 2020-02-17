from abc import ABCMeta, abstractmethod


class SensorData:
    """Wrapper for sensor results
    """
    pass


class BaseSensor(metaclass=ABCMeta):
    @abstractmethod
    def connect(self, timeout: int):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def data_ready(self) -> bool:
        pass

    @abstractmethod
    def get_data(self) -> SensorData:
        pass
