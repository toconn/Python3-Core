import unittest
from ua.core.utils import objectconditions


class TestClass:
    def __init__ (self, name = None, path = None, count = None):
        self.name = name
        self.path = path
        self.count = count

FIELD_NAME = "name"


MATCH_NAME_ITEM_1 = "1.1"
MATCH_NAME_NONE = "No Match"

MATCH_NAME_1_ALL = "Test"
MATCH_NAME_2_ALL = "Item"
MATCH_NAME_3_ITEM_1_2 = ".1"

TEST_ITEM_1 = TestClass ("Test 1.1 Item", "", 1)
TEST_ITEM_2 = TestClass ("Test 2.1 Item", "", 2)
TEST_ITEM_3 = TestClass ("Test 3.2 Item", "", 3)

TEST_ITEMS = [
        TEST_ITEM_1,
        TEST_ITEM_2,
        TEST_ITEM_3
        ]

EXPECTED_ITEMS_NONE = []

EXPECTED_ITEMS_1 = [
        TEST_ITEM_1
        ]

EXPECTED_ITEMS_1_2 = [
        TEST_ITEM_1,
        TEST_ITEM_2
        ]


class Test_ObjectFilter(unittest.TestCase):
    
    def test_filterOnAndCondition_MatchAll(self):
        
        condition=objectconditions.andConditions(
                objectconditions.containsText(FIELD_NAME, MATCH_NAME_1_ALL),
                objectconditions.containsText(FIELD_NAME, MATCH_NAME_2_ALL)                               
                )
        self._call_and_test_conditons(condition, TEST_ITEMS, TEST_ITEMS)

    def test_filterOnAndCondition_Match2(self):
        
        condition=objectconditions.andConditions(
                objectconditions.containsText(FIELD_NAME, MATCH_NAME_1_ALL),
                objectconditions.containsText(FIELD_NAME, MATCH_NAME_3_ITEM_1_2)                               
                )
        self._call_and_test_conditons(condition, TEST_ITEMS, EXPECTED_ITEMS_1_2)

    def test_filterOnAndCondition_MatchNone(self):
        
        condition=objectconditions.andConditions(
                objectconditions.containsText(FIELD_NAME, MATCH_NAME_1_ALL),
                objectconditions.containsText(FIELD_NAME, MATCH_NAME_NONE)                               
                )
        self._call_and_test_conditons(condition, TEST_ITEMS, EXPECTED_ITEMS_NONE)

    def test_filterOnContainsText(self):
        
        condition = objectconditions.containsText(FIELD_NAME, MATCH_NAME_ITEM_1)
        self._call_and_test_conditons(condition, TEST_ITEMS, EXPECTED_ITEMS_1)

    def test_filterOnContainsTextNoMatch(self):
        
        condition = objectconditions.containsText(FIELD_NAME, MATCH_NAME_NONE)
        self._call_and_test_conditons(condition, TEST_ITEMS, EXPECTED_ITEMS_NONE)

    def _call_and_test_conditons (self, condition, test_items, expected_items):
        
        actual_items = [item for item in test_items if condition (item)]
        self.assertListEqual(expected_items, actual_items, "Filtered lists do not match.")

        