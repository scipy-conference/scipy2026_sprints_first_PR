def fibonacci(max):
    values = [0, 1]
    while values[-2] + values[-1] < max:
        values.append(values[-2] + values[-1])
    return values


def factorial(value):
    if value == 0:
        return 1
    elif value < 0:
        raise RuntimeError(f"Cannot find factorial for negative {value=}")
    else:
        return value * factorial(value - 1)
