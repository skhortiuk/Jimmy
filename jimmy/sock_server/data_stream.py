import logging
import socket
from typing import Dict, Union

from jimmy.sensors.base import SensorData


class DataStream:
    logger = logging.getLogger()

    def __init__(self):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def stream_data(self, data: Dict[Union[str, SensorData]]):
        pass
