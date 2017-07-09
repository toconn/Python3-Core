import unittest
from ua.core.test.testutils import *
from ua.core.utils import objectconditions

class TestClass:
    def __init__ (self, name = None, path = None, count = None):
        self.name = name
        self.path = path
        self.count = count

FIELD_PATH = "path"

MATCH_FILE_NO_MATCH = "No match"
MATCH_FILE_NAME = "Test-File-1.text"
MATCH_SUBDIRECTORY_NAME = "Subdirectory 1"

test_dir = os.path.join (TEST_DIR, "Test Directories")

TEST_ITEM_1 = TestClass ("Test 1 Directory", os.path.join (test_dir, "Directory 1"), 1)
TEST_ITEM_2 = TestClass ("Test 2 Directory", os.path.join (test_dir, "Directory 2"), 2)
TEST_ITEM_3 = TestClass ("Test 3 Directory", os.path.join (test_dir, "Directory 3"), 3)


TEST_ITEMS = [
        TEST_ITEM_1,
        TEST_ITEM_2,
        TEST_ITEM_3
        ]

# Results for TEST_FILE_NAME, TEST_SUBDIRECTORY_NAME
EXPECTED_ITEMS_NONE = []

EXPECTED_ITEMS_1_2 = [
        TEST_ITEM_1,
        TEST_ITEM_2
        ]


class Test_Integrated_ObjectFilter(unittest.TestCase):

    def test_filterOnContainsDir(self):
        
        condition = objectconditions.containsDir(FIELD_PATH, MATCH_SUBDIRECTORY_NAME)
        
        print (os.path.join (TEST_ITEM_1.path, MATCH_SUBDIRECTORY_NAME))
        self._call_and_test_condition(condition, TEST_ITEMS, EXPECTED_ITEMS_1_2)

    def test_filterOnContainsDirNoMatch(self):
        
        condition = objectconditions.containsDir(FIELD_PATH, MATCH_FILE_NO_MATCH)
        self._call_and_test_condition(condition, TEST_ITEMS, EXPECTED_ITEMS_NONE)

    def test_filterOnContainsDirNotDirectory(self):
        
        condition = objectconditions.containsDir(FIELD_PATH, MATCH_FILE_NAME)
        self._call_and_test_condition(condition, TEST_ITEMS, EXPECTED_ITEMS_NONE)

    def test_filterOnContainsFile(self):
        
        condition = objectconditions.containsFile(FIELD_PATH, MATCH_SUBDIRECTORY_NAME)
        
        print (os.path.join (TEST_ITEM_1.path, MATCH_FILE_NAME))
        self._call_and_test_condition(condition, TEST_ITEMS, EXPECTED_ITEMS_1_2)

    def test_filterOnContainsFileNoMatch(self):
        
        condition = objectconditions.containsFile(FIELD_PATH, MATCH_FILE_NO_MATCH)
        self._call_and_test_condition(condition, TEST_ITEMS, EXPECTED_ITEMS_NONE)

    def _call_and_test_condition (self, condition, test_items, expected_items):
        
        actual_items = [item for item in test_items if condition (item)]
        self.assertListEqual(expected_items, actual_items, "Filtered lists do not match.")

