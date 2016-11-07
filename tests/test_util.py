import sys
import os
import unittest

import pandas as pd
import numpy as np

from vaquero.util import *

THIS_DIR = os.path.dirname(os.path.realpath(__file__))


class TestUtil(unittest.TestCase):
    def test_first(self):
        def f():
            yield 10
            yield 20

        self.assertEqual(first(f()), 10)

    def test_jsonlines_reader(self):
        reader = jsonlines_reader(os.path.join(THIS_DIR, "demo.jsonlines"))
        expected = [{"first": "Bob", "age": 32},
                    {"first": "Alice", "age": 33}]
        self.assertEqual(list(reader), expected)

    def test_pd_print_entirely(self):
        if not hasattr(sys.stdout, "getvalue"):
            self.fail("need to run in buffered mode")
        series = pd.Series(range(1000))
        pd_print_entirely(series)
        self.assertEqual(1001, len(sys.stdout.getvalue().splitlines()))

    def test_examine_pairwise_res(self):
        src = {'x': 100}

        def f(s, d):
            d['x'] = s['x'] ** 2

        res = examine_pairwise_result(f, src)
        self.assertEqual(res['x'], 10000)

    def test_np_and(self):
        x = np.arange(10)
        res = list(x[np_and(x > 5, x % 2 == 0)])
        self.assertEqual(res, [6, 8])

    def test_np_or(self):
        x = np.arange(10)
        res = list(x[np_or(x > 5, x % 2 == 0)])
        self.assertEqual(res, [0, 2, 4, 6, 7, 8, 9])