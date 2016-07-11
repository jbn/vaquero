import numpy as np
from functools import reduce


def np_and(condition, *conditions):
    # This is just much less noise then (a) && (b) && (c) to me.
    return reduce(np.logical_and, conditions, condition)


def np_or(condition, *conditions):
    # This is just much less noise then (a) || (b) || (c) to me.
    return reduce(np.logical_or, conditions, condition)

