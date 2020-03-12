from abc import abstractmethod, ABC


class SensorData:
    """Wrapper for sensor results
    """
    pass


class BaseSensor(ABC):
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
