import sys
import os
import unittest
import pandas as pd

from vaquero.io import *

THIS_DIR = os.path.dirname(os.path.realpath(__file__))


class TestIO(unittest.TestCase):
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
