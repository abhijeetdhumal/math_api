from numbers import Number
from typing import List
import heapq
import math


def get_minimum(values: List[Number], n: int):
    return heapq.nsmallest(n, values)


def get_maximum(values: List[Number], n: int):
    return heapq.nlargest(n, values)


def calc_average(values: List[Number]):
    length = len(values)
    return sum(values)/length


def calc_percentile(values: List[Number], n: int):
    idx = int(math.ceil((len(values) * n) / 100)) - 1
    print(idx)
    percentile = sorted(values)[idx]
    return percentile


def get_median(values):
    values.sort()
    length = len(values)
    mid = int(length/2)
    if length % 2 == 0:
        median = (values[mid] + values[mid - 1]) / 2
    else:
        median = values[mid]
    return median
