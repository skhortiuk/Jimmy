from time import time


def millis() -> int:
    return int(round(time() * 1000))


def frequency_to_ms(frequency: int):
    return 1000 / frequency
