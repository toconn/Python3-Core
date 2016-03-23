import unittest
from ua.core.utils import dictutils


class Test_DictUtils(unittest.TestCase):

    def test_max_key_len_4(self):
        dict1 = {'1':'x', '22':'x', '4444':'x', '333': 'x'}
        self.assertEqual(dictutils.max_key_len(dict1), 4)

    def test_max_key_len_empty(self):
        dict1 = {}
        self.assertEqual(dictutils.max_key_len(dict1), 0)

    def test_max_key_len_none(self):
        self.assertEqual(dictutils.max_key_len(None), 0)
