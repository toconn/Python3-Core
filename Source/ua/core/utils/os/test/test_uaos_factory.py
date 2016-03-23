import unittest

from ua.core.utils.os import os_const
from ua.core.utils.os import ua_os_factory

from ua.core.utils.os import UaOsLinux
from ua.core.utils.os import UaOsOsx
from ua.core.utils.os import UaOsWindows

class TestOsFactory (unittest.TestCase):
    
    def test_create_os_empty(self):
        self._test_create_os_utils(' ', None)
    
    def test_create_os_linux(self):
        self._test_create_os_utils(os_const.OS_NAME_LINUX, UaOsLinux.__name__)
    
    def test_create_os_no_param(self):
        os = ua_os_factory.create_ua_os()
        self.assertTrue(os) # Must have a value.
    
    def test_create_os_osx(self):
        self._test_create_os_utils(os_const.OS_NAME_OSX, UaOsOsx.__name__)
    
    def test_create_os_windows(self):
        self._test_create_os_utils(os_const.OS_NAME_WINDOWS, UaOsWindows.__name__)
    
    def _test_create_os_utils(self, os_name, os_type):
    
        os = ua_os_factory.create_ua_os(os_name)
        
        if os_type is None:
            self.assertIsNone(os, "Expected OS to be None.")
        else:
            self.assertEquals (os_type, os.__class__.__name__)
            
            