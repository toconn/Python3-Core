import unittest
from ua.core.utils import listutils

class TestListUtils(unittest.TestCase):
    
    def test_count_empty(self):
        
        count = listutils.count (None)
        self.assertEquals(count, 0)
        
    def test_count_non_empty(self):
        
        count = listutils.count ([1, 2, 3])
        self.assertEquals(count, 3)
        
