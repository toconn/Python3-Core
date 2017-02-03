import unittest
from ua.core.utils import listutils

class TestListUtils(unittest.TestCase):
    
    def test_count_empty(self):
        
        count = listutils.count (None)
        self.assertEquals(count, 0)
        
    def test_count_non_empty(self):
        
        count = listutils.count ([1, 2, 3])
        self.assertEquals(count, 3)
        
    def test_is_equal_none_none(self):
        
        result = listutils.is_equal(None, None)
        self.assertTrue(result)
        
    def test_is_equal_none_empty(self):
        
        result = listutils.is_equal(None, [])
        self.assertFalse(result)
        
    def test_is_equal_empty_none(self):
        
        result = listutils.is_equal([], None)
        self.assertFalse(result)
        
    def test_is_equal_match(self):
        
        result = listutils.is_equal([1, '2', 'THREE'], [1, '2', 'THREE'])
        self.assertTrue(result)
        
    def test_is_equal_no_match(self):
        
        result = listutils.is_equal([1, '2', 'THREE'], [1, '2', 'FOUR'])
        self.assertFalse(result)
        
    def test_is_equal_no_match_diff_lengths(self):
        
        result = listutils.is_equal([1, '2', 'THREE'], [1, '2', 'THREE', 4])
        self.assertFalse(result)
        
