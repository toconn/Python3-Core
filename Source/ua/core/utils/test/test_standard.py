import unittest
from ua.core.utils.standard import *

class TestStandard(unittest.TestCase):
    
    FALSE_RESULT = 'It is false'
    TRUE_RESULT = 'It is True'
    
    def test_iif_false(self):
        self._test_iif (test_value = False, expected_result = TestStandard.FALSE_RESULT)
        
    def test_iif_false_none(self):
        result = iif (False, TestStandard.TRUE_RESULT)   # No false value passed in
        self.assertIsNone(result)
        
    def test_iif_true(self):
        self._test_iif (test_value = True, expected_result = TestStandard.TRUE_RESULT)
        
    def _test_iif(self, test_value, expected_result):
        result = iif (test_value, TestStandard.TRUE_RESULT, TestStandard.FALSE_RESULT)
        self.assertEquals(expected_result, result)
        