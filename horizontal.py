import math
from typing import Optional, Dict, Any, Tuple
import numpy as np
import pandas as pd


class HorizontalProjection:
    def __init__(
            self,
            g: float = 9.81,
            v0: Optional[float] = None,
            h0: Optional[float] = None,
            t: Optional[float] = None,
            s: Optional[float] = None,
    ):
        self.g = g
        self.v0 = v0
        self.h0 = h0
        self.t = t
        self.s = s

        values_given = sum(val is not None for val in [v0, h0, t, s])
        if values_given != 2:
            raise ValueError("You need to add at least 2 values: v0, h0, t or s.")

        self.calculate()

    def calculate(self):
        if self.v0 is not None and self.t is not None and self.h0 is None and self.s is None:
            self.h0 = (self.g * pow(self.t, 2)) / 2
            self.s = self.v0 * math.sqrt((2 * self.h0) / self.g)
        elif self.v0 is not None and self.h0 is not None and self.t is None and self.s is None:
            self.t = math.sqrt((2 * self.h0) / self.g)
            self.s = self.v0 * self.t
        elif self.v0 is not None and self.s is not None and self.t is None and self.h0 is None:
            self.t = self.s / self.v0
            self.h0 = (self.g * pow(self.t, 2)) / 2
        elif self.h0 is not None and self.s is not None and self.t is None and self.v0 is None:
            self.t = math.sqrt((2 * self.h0) / self.g)
            self.v0 = self.s / self.t

    def get_position_at_time(self, time: float) -> Tuple[float, float]:
        if self.v0 is not None and self.t is not None:
            x = self.v0 * time
            y = self.h0 - (0.5 * self.g * pow(time, 2))
            return x, y
        else:
            raise ValueError("You need to calculate v0 and t first.")

    def calc(self) -> Dict[str, Any]:
        return {
            "v0": self.v0,
            "h0": self.h0,
            "t": self.t,
            "s": self.s,
        }


def create_trajectory_dataframe(hp: HorizontalProjection, num_points: int = 1000) -> pd.DataFrame:
    max_time = hp.t
    times = np.linspace(0, max_time, num=num_points)
    positions = [hp.get_position_at_time(t) for t in times]
    x_values, y_values = zip(*positions)

    data = {'Time': times, 'X': x_values, 'Y': y_values}
    df = pd.DataFrame(data)

    return df


if __name__ == '__main__':
    hp = HorizontalProjection(v0=20, t=3.5)
    print(hp.calc())

    trajectory_df = create_trajectory_dataframe(hp)
    print(trajectory_df)