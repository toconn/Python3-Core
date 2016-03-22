import unittest
from ua.utils import strutils


class Test_StrUtils(unittest.TestCase):
    
    def test_lower_none(self):

        result = strutils.lower(None)
        self.assertIsNone(result)

    def test_lower_lower(self):
    
        result = strutils.lower('abc123')
        self.assertEquals('abc123', result)

    def test_lower_upper(self):
    
        result = strutils.lower('ABC123')
        self.assertEquals('abc123', result)

    def test_replace_int(self):
        
        result = strutils.replace('AB12CD12ED12', '12', 34)
        self.assertEquals(result, 'AB34CD34ED34')

    def test_replace_none(self):
        
        result = strutils.replace(None, None, None)
        self.assertIsNone(result, 'Expected None.')

    def test_replace_standard(self):
        
        result = strutils.replace('AB12CD12ED12', '12', '34')
        self.assertEquals(result, 'AB34CD34ED34')

    def test_strip_none(self):
        
        result = strutils.strip(None)
        self.assertIsNone(result, 'Expected None.')
    
    def test_strip_text_has_whitespace(self):
        
        result = strutils.strip('    abcd  \t\n ')
        self.assertEquals(result, 'abcd')
        
    def test_strip_text_no_whitespace(self):
        
        result = strutils.strip('abcd')
        self.assertEquals(result, 'abcd', 'Expected no change.')
