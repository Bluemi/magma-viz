import numpy as np


def get_circle_positions(n: int) -> np.ndarray:
    """
    Creates a numpy array with shape [n, 2], where each row is a position in a circle.
    :param n: The number of positions to generate.
    :return: Positions arranged in a circle.
    """
    degrees = np.linspace(0, np.pi * 2, n, endpoint=False)
    x = np.cos(degrees)
    y = np.sin(degrees)
    return np.stack([x, y], axis=1)


def get_line_positions(n: int) -> np.ndarray:
    x = np.linspace(0, n, n)
    y = np.zeros(n)
    return np.stack([x, y], axis=1)