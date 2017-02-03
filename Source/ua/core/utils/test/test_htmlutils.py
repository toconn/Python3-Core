import unittest
from ua.core.utils import htmlutils


class Test_HtmlUtils(unittest.TestCase):
    
    def test_strip_tags_none(self):
        
        result = htmlutils.strip_tags(None)
        self.assertIsNone(result)
    
    def test_strip_tags_match(self):
        
        result = htmlutils.strip_tags('text <tag>tag content</tag> more text <another tag>tag content</another tag> the end.<br/>')
        self.assertEquals('text tag content more text tag content the end.', result)
    
    def test_strip_tags_no_tags(self):
        
        result = htmlutils.strip_tags('This is text.')
        self.assertEquals('This is text.', result)
