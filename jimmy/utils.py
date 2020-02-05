from time import time


def millis() -> int:
    """
    Returns:
        Current time in milliseconds
    """
    return int(round(time() * 1000))


def frequency_to_ms(frequency: int) -> int:
    """
    Args:
        frequency: in Hz

    Returns:
        Number of milliseconds equals to frequency in Hz
    """
    return int(round(1000 / frequency))
