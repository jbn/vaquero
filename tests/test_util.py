import unittest
import numpy as np

from vaquero.util import *


class TestUtil(unittest.TestCase):
    def test_np_and(self):
        x = np.arange(10)
        res = list(x[np_and(x > 5, x % 2 == 0)])
        self.assertEqual(res, [6, 8])

    def test_np_or(self):
        x = np.arange(10)
        res = list(x[np_or(x > 5, x % 2 == 0)])
        self.assertEqual(res, [0, 2, 4, 6, 7, 8, 9])
