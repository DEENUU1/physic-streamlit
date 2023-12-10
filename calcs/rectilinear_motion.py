import math
from typing import Optional


def calculate_displacement(xs: float, xe: float) -> float:
    return xe - xs


def calculate_average_speed(xe: float, xs: float, te: float, ts: float) -> float:
    return calculate_displacement(xs, xe) / (te - ts)

