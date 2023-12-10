import math
from typing import Optional


def calculate_displacement(xs: float, xe: float) -> float:
    # Xe - Xs
    return xe - xs


def calculate_average_speed(xe: float, xs: float, te: float, ts: float) -> float:
    # Xe - Xs / Te - Ts
    return calculate_displacement(xs, xe) / (te - ts)


def calculate_avg_acceleration(ve: float, vs: float, te: float, ts: float) -> float:
    # Ve - Vs / Te - Ts
    return (ve - vs) / (te - ts)
