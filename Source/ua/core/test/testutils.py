import os

class TestItem:
    """ 
        Created with CodeCrank.io
    """

    def __init__ (self, name = None, count = None, enabled = None):

        self.name = name
        self.count = count
        self.enabled = enabled

    def __repr__ (self):

        return "TestItem [" + \
            "name=" + (self.name if self.name is not None else "[None]") + \
            ", count=" + (str(self.count) if self.count is not None else "[None]") + \
            ", enabled=" + (str(self.enabled) if self.enabled is not None else "[None]") + \
            "]"

TEST_DIR = os.path.expandvars('${User_Dev_Dir}/Core - Python/Data - Test')