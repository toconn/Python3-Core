import unittest
from ua.core.utils import strutils


class Test_StrUtils(unittest.TestCase):
    
    def test_before_none(self):
        
        result = strutils.before(None, 'break')
        self.assertIsNone(result)
    
    def test_before_match(self):
        
        result = strutils.before('ABCbreak123', 'break')
        self.assertEquals('ABC', result)
    
    def test_before_no_match(self):
        
        result = strutils.before('ABC123', 'break')
        self.assertEquals('ABC123', result)

    def test_contains_none(self):
        
        result = strutils.contains(None, 'match')
        self.assertFalse(result)
    
    def test_contains_match(self):
        
        result = strutils.contains('ABCmatch123', 'match')
        self.assertTrue(result)
    
    def test_contains_no_match(self):
        
        result = strutils.contains('ABC123', 'match')
        self.assertFalse(result)
    
    def test_contains_ignore_case_none(self):
        
        result = strutils.contains_ignore_case(None, 'match')
        self.assertFalse(result)
    
    def test_contains_ignore_case_match(self):
        
        result = strutils.contains_ignore_case('ABCmaTCh123', 'MAtcH')
        self.assertTrue(result)
    
    def test_contains_ignore_case_no_match(self):
        
        result = strutils.contains_ignore_case('ABC123', 'match')
        self.assertFalse(result)
    
    def test_ends_with_none(self):
        
        result = strutils.ends_with(None, 'end')
        self.assertFalse(result)
    
    def test_ends_with_match(self):
        
        result = strutils.ends_with('ABC123end', 'end')
        self.assertTrue(result)
    
    def test_ends_with_no_match(self):
        
        result = strutils.ends_with('ABC123', 'end')
        self.assertFalse(result)
        
    def test_equals_ignore_case_None_None(self):
    
        result = strutils.equals_ignore_case (None, None)
        self.assertTrue (result)
    
    def test_equals_ignore_case_None_Value(self):
    
        result = strutils.equals_ignore_case (None, '123')
        self.assertFalse (result)
    
    def test_equals_ignore_case_Value_None(self):
    
        result = strutils.equals_ignore_case ('123', None)
        self.assertFalse (result)
    
    def test_equals_ignore_case_lower_case(self):
    
        result = strutils.equals_ignore_case ('abcd', 'abcd')
        self.assertTrue (result)
    
    def test_equals_ignore_case_mixed_case(self):
    
        result = strutils.equals_ignore_case ('aBcD', 'AbCd')
        self.assertTrue (result)
    
    def test_equals_ignore_case_no_match(self):
    
        result = strutils.equals_ignore_case ('abcd', 'dcba')
        self.assertFalse (result)
    
    def test_equals_ignore_case_upper_case(self):
    
        result = strutils.equals_ignore_case ('ABCD', 'ABCD')
        self.assertTrue (result)
    
    def test_join(self):
        
        result = strutils.join (['aa', 'bb', 'cc'], '-')
        self.assertEquals (result, 'aa-bb-cc')
    
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