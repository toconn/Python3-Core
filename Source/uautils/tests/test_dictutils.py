import unittest
from uautils import dictutils


class Test_DictUtils(unittest.TestCase):

    def test_max_key_len(self):

        dict1 = {'1':'x', '22':'x', '4444':'x', '333': 'x'}
        self.assertEqual(dictutils.max_key_len(dict1), 4)
