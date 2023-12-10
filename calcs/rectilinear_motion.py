import math
import pandas as pd


def calculate_displacement(xs: float, xe: float) -> float:
    # Xe - Xs
    return xe - xs


def calculate_average_speed(xe: float, xs: float, te: float, ts: float) -> float:
    # Xe - Xs / Te - Ts
    return calculate_displacement(xs, xe) / (te - ts)


def calculate_avg_acceleration(ve: float, vs: float, te: float, ts: float) -> float:
    # Ve - Vs / Te - Ts
    return (ve - vs) / (te - ts)


def calculate_free_fall_total_time(h: float, g: float = 9.81) -> float:
    # sqrt(2*h / g)
    return math.sqrt((2 * h) / g)


def calculate_free_fall_ending_speed(h: float, g: float = 9.81) -> float:
    # sqrt(2*h*g)
    return math.sqrt(2 * h * g)


def free_fall_trajectory(t: float, g: float = 9.81) -> pd.DataFrame:
    times = []
    speeds = []

    for t in range(int(t) + 1):
        time = float(t)
        speed = g * time
        times.append(time)
        speeds.append(speed)

    return pd.DataFrame({'time': times, 'speed': speeds})
