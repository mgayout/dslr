import numpy as np # type: ignore


def count_(data):
    return len(data)


def mean_(data):
    total = 0
    for d in data:
        if np.isnan(d):
            continue
        total += d
    return total / len(data)


def std_(data, mean):
    total = 0
    for d in data:
        if np.isnan(d):
            continue
        total += pow(d - mean, 2)
    return pow(total / (len(data)), 0.5)


def percentile_(data, p):
    idx = (len(data) - 1) * (p / 100)
    if isinstance(idx, int):
        return data[idx]
    idx_min = int(idx)
    idx_max = idx_min + 1
    return (data[idx_min] * (idx_max - idx) + data[idx_max] * (idx - idx_min))
