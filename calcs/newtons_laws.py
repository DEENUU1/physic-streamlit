from typing import Optional, Dict


def second_law(m: Optional[float] = None, f: Optional[float] = None, a: Optional[float] = None) -> Dict[str, float]:
    count_args = sum(arg is not None for arg in [f, a])

    if count_args == 0:
        raise Exception("You must specify at least one of the following arguments: f, a")

    if not m:
        raise Exception("m argument is required")

    m = m
    f = f
    a = a

    if f:
        a = f / m

    if a:
        f = m * a

    return {
        "f": f,
        "a": a,
        "m": m,
    }

