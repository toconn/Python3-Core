import unittest
from ua.core.utils.os import UaOsWindows
from . import test_data

class TestWindowsOS(unittest.TestCase):
    
    def setUp(self):
        self._os = UaOsWindows()
        
    def test_class_constants(self):
        self.assertTrue (self._os.FILE_SEPARATOR)
        self.assertTrue (self._os.NEWLINE)
        self.assertTrue (self._os.OS_NAME)
        self.assertTrue (self._os.PATH_SEPARATOR)
    
    def test_normalize_path_none(self):
        self._test_normaliz_path ('', '')
    
    def test_normalize_path_linux(self):
        self._test_normaliz_path (test_data.DIR_LINUX_1, test_data.DIR_WINDOWS_1)
    
    def test_normalize_path_osx(self):
        self._test_normaliz_path (test_data.DIR_OSX_1, test_data.DIR_WINDOWS_1)
    
    def test_normalize_path_windows(self):
        self._test_normaliz_path (test_data.DIR_WINDOWS_1, test_data.DIR_WINDOWS_1)
    
    def _test_normaliz_path(self, path, expected_normalized_path):
        
        actual_normalized_path = self._os.normalize_path (path)
        self.assertEquals (expected_normalized_path, actual_normalized_path, 'The actual path did not match the expected path.')
