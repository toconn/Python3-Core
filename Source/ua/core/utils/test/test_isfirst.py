import unittest
from ua.core.utils import isfirst


class Test_IsFirst(unittest.TestCase):

    def test_isFirst(self):

        first = isfirst.IsFirst()

        self.assertTrue(first.isirst())
        self.assertFalse(first.is_first())
        self.assertFalse(first.is_first())

    def test_isFirst(self):

        first = isfirst.IsFirst()

        self.assertFalse(first.is_not_first())
        self.assertTrue(first.is_not_first())
        self.assertTrue(first.is_not_first())
