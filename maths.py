import numpy as np # type: ignore


def count_(data):
    return len(data)


def mean_(data):
    total = 0
    for d in data:
        if isinstance(d, (str)) or np.isnan(d):
            return 0
        total += d
    return total / len(data)


def std_(data):
    n = len(data)
    if n < 2:
        return 0
    total = 0
    for d in data:
        if isinstance(d, (str)) or np.isnan(d):
            return 0
        total += d
        
    return 0


def min_(data):
    return 0


def q1_(data):
    return 0


def median_(data):
    return 0


def q3_(data):
    return 0


def max_(data):
    return 0