import unittest
from ua.core.utils import strlistutils

class TestStrListUtils (unittest.TestCase):
    
    TEST_LIST_1 = ['a', 'b', 'c']
    
    def test_find_index_containing_none_none (self):
    
        result = strlistutils.find_index_containing(None, None)
        self.assertEquals(result, -1)
    
    def test_find_index_containing_none_value (self):
    
        result = strlistutils.find_index_containing(None, 'match')
        self.assertEquals(result, -1)
    
    def test_find_index_containing_value_none (self):
    
        result = strlistutils.find_index_containing(self.TEST_LIST_1, None)
        self.assertEquals(result, -1)

    def test_find_index_containing_match (self):
    
        result = strlistutils.find_index_containing(self.TEST_LIST_1, 'b')
        self.assertEquals(result, 1)

    def test_find_index_containing_no_match (self):
    
        result = strlistutils.find_index_containing(self.TEST_LIST_1, 'no match')
        self.assertEquals(result, -1)

    def test_find_index_containing_ignore_case_none_none (self):
    
        result = strlistutils.find_index_containing_ignore_case(None, None)
        self.assertEquals(result, -1)
    
    def test_find_index_containing_ignore_case_none_value (self):
    
        result = strlistutils.find_index_containing_ignore_case(None, 'match')
        self.assertEquals(result, -1)
    
    def test_find_index_containing_ignore_case_value_none (self):
    
        result = strlistutils.find_index_containing_ignore_case(self.TEST_LIST_1, None)
        self.assertEquals(result, -1)

    def test_find_index_containing_ignore_case_match (self):
    
        result = strlistutils.find_index_containing_ignore_case(self.TEST_LIST_1, 'B')
        self.assertEquals(result, 1)

    def test_find_index_containing_ignore_case_no_match (self):
    
        result = strlistutils.find_index_containing_ignore_case(self.TEST_LIST_1, 'no match')
        self.assertEquals(result, -1)
