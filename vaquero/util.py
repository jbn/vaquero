from __future__ import print_function

import os
import json
import numpy as np
import pandas as pd
from fnmatch import fnmatch
from functools import reduce
from collections import OrderedDict


def first(items):
    """
    Get the first item from an iterable.

    Warning: It consumes from a generator.

    :param items: an iterable
    :return: the first in the iterable
    """
    for item in items:
        return item


def nth(items, i):
    """
    Get the nth item from an iterable.

    Warning: It consumes from a generator.

    :param items: an iterable
    :return: the first in the iterable
    """
    for j, item in enumerate(items):
        if j == i:
            return item


def tap(items, f=print):
    """
    Apply f (default=print) to each item in items then yield the item.


    :param items: an iterable
    :param f: function to call for each item in items

    """
    for item in items:
        f(item)
        yield item


def find(items, predicate):
    """
    Find the item in an iterable.

    :param items: an iterable
    :param predicate: a function which returns true if it matches your query
    :return: the first item which matched the predicate, else None
    """
    for item in items:
        if predicate(item):
            return item
    return None


def jsonlines_reader(file_path, skip_decode_errors=False):
    """
    Yield each document in a JSON-lines document.
    :param file_path: filepath to a json-lines file set
    """
    with open(file_path) as fp:
        for line in fp:
            try:
                yield json.loads(line)
            except ValueError:
                if not skip_decode_errors:
                    raise


def examine_pairwise_result(f, input_doc):
    """
    Test f against input doc and return the resulting dict.

    :param f: a function with a `f(src_obj, dst_dict)` signature
    :param input_doc: the input object
    :return: a dictionary populated via f
    """
    d = OrderedDict()
    f(input_doc, d)
    return d


def files_processor(generator_func, dir_path, shell_ptn="*", recursive=False):
    for file_name in os.listdir(dir_path):
        file_path = os.path.join(dir_path, file_name)
        if recursive and os.path.isdir(file_path):
            for item in files_processor(generator_func, file_path,
                                        shell_ptn, True):
                yield item
        else:
            if fnmatch(file_name, shell_ptn):
                for item in generator_func(file_path):
                    yield item


def pd_print_entirely(frame_or_series):
    """
    Print a pandas dataframe or series in its entirety.

    :param frame_or_series: a pandas Series or DataFrame
    """
    columns = pd.get_option('display.max_columns')
    pd.set_option('display.max_columns', None)

    rows = pd.get_option('display.max_rows')
    pd.set_option('display.max_rows', None)

    try:
        print(frame_or_series)
    finally:
        pd.set_option('display.max_columns', columns)
        pd.set_option('display.max_rows', rows)


def np_and(condition, *conditions):
    # This is just much less noise then (a) && (b) && (c) to me.
    return reduce(np.logical_and, conditions, condition)


def np_or(condition, *conditions):
    # This is just much less noise then (a) || (b) || (c) to me.
    return reduce(np.logical_or, conditions, condition)


class deferred_delete:
    """
    Context manager for performing deferred deletes on some dictionary.

    Generally useful for identifying which keys to delete in a loop, then
    having them automatically deleted later, since you can't delete
    mid-iteration (a RuntimeError).

    Deletions execute in order. And, multiple calls to delete are possible.
    """

    def __init__(self, obj, skip_missing=True):
        """

        :param obj: the dictionary (or some object implementing `__delitem__`)
        :param skip_missing: if True then the deferred operation only calls
            the delete if the key is present in the underlying object
        """
        self._d = obj
        self._ks = []
        self._skip_missing = skip_missing
        self._executed_deletions = 0

    def __enter__(self):
        self._executed_deletions = 0
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        for k in self._ks:
            if not self._skip_missing or k in self._d:
                self._executed_deletions += 1
                del self._d[k]

    def __delitem__(self, k):
        self._ks.append(k)

    @property
    def executed_deletions(self):
        return self._executed_deletions
