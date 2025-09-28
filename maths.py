import numpy as np # type: ignore


def count_(data):
    count = 0
    for d in data:
        if isinstance(d, (int, float, np.floating)) and not np.isnan(d):
            count += 1
        elif isinstance(d, (str)):
            count += 1
    return count


def mean_(data):
    return sum(data) / len(data)


def std_(data, mean):
    return (sum((d - mean) ** 2 for d in data) / len(data)) ** 0.5


def percentile_(data, p):
    data.sort()
    idx = (len(data) - 1) * (p / 100)
    if idx.is_integer():
        return data[int(idx)]
    i = int(idx)
    return data[i] * (i + 1 - idx) + data[i + 1] * (idx - i)
