import unittest
from ua.core.utils import autoincr

class Test_AutoIncr(unittest.TestCase):

    def test_autoIncr_default(self):

        auto_incr = autoincr.AutoIncr()
        self.assertEqual (auto_incr.next(), 0)
        self.assertEqual (auto_incr.next(), 1)
        self.assertEqual (auto_incr.next(), 2)

    def test_autoIncr_start_11(self):

        auto_incr = autoincr.AutoIncr(11)
        self.assertEqual (auto_incr.next(), 11)
        self.assertEqual (auto_incr.next(), 12)
