import math
from typing import Optional, Dict, Any


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

    def calc(self) -> Dict[str, Any]:
        return {
            "v0": self.v0,
            "h0": self.h0,
            "t": self.t,
            "s": self.s,
        }


if __name__ == '__main__':
    hp = HorizontalProjection(v0=10, t=10)
    print(hp.calc())
