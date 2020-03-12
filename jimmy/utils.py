from time import time

from jimmy.config import SECOND


def millis() -> int:
    """
    Returns:
        Current time in milliseconds
    """
    return int(round(time() * SECOND))


def frequency_to_ms(frequency: int) -> int:
    """
    Args:
        frequency: in Hz

    Returns:
        Number of milliseconds equals to frequency in Hz
    """
    return int(round(SECOND / frequency))
