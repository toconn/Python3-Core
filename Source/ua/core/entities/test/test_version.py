import unittest
from ua.core.entities.version import Version

class TestVersion(unittest.TestCase):
    
    def test_instantiate_No_Param(self):
        
        version = Version()
        self.assertEquals (version.version_string, '0.0.0')
        
    def test_instantiate_Num_Params(self):
        
        version = Version(1, 2, 3)
        self.assertEquals (version.version_string, '1.2.3')
        
    def test_instantiate_String_Param(self):
        
        version = Version('1.2.3')
        self.assertEquals (version.version_string, '1.2.3')

    def test_instantiate_String_Param_check_nums(self):
        
        version = Version('1.2.3')
        self.assertEquals (version.major, 1)
        self.assertEquals (version.minor, 2)
        self.assertEquals (version.revision, 3)

    def test_version_string_check_nums(self):
        
        version = Version()
        version.version_string = '1.2.3'
        self.assertEquals (version.major, 1)
        self.assertEquals (version.minor, 2)
        self.assertEquals (version.revision, 3)
