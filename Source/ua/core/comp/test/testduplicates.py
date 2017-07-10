import unittest
from ua.core.test.testutils import TestItem;

from ua.core.comp.duplicates import DuplicateTracker

NAME_1 = "Item 1"
NAME_1_2 = "Item 1.2"
NAME_1_3 = "Item 1.3"
NAME_2 = "Item 2"

ITEM_1_1 = TestItem (NAME_1, 1, True)
ITEM_1_2 = TestItem (NAME_1_2, 1, True)
ITEM_1_3 = TestItem (NAME_1_3, 1, True)
ITEM_2 = TestItem (NAME_2, 2, False)

class TestDuplicateTracker (unittest.TestCase):

    def setUp(self):
        
        self._empty_duplicate_tracker = DuplicateTracker()
        self._single_item_duplicate_tracker = DuplicateTracker()
        self._single_item_duplicate_tracker.add(NAME_1, ITEM_1_1)

    def test_adding_existing_item_to_tracker_creates_duplicate(self):

        self._single_item_duplicate_tracker.add(NAME_1, ITEM_1_2)
        self.assertTrue(self._single_item_duplicate_tracker.has_duplicates())
    
    def test_adding_three_similar_items_returns_duplicate_list_of_three_items(self):
        
        self._empty_duplicate_tracker.add(NAME_1, ITEM_1_1)
        self._empty_duplicate_tracker.add(NAME_1, ITEM_1_2)
        self._empty_duplicate_tracker.add(NAME_1, ITEM_1_3)
        
        duplicates_dict = self._empty_duplicate_tracker.duplicates_dict()
        duplicates = duplicates_dict[NAME_1]
        duplicates_set = set (duplicates)
        
        self.assertEquals (len (duplicates_dict), 1)
        self.assertEquals (len (duplicates), 3)
        self.assertTrue (ITEM_1_1 in duplicates_set)
        self.assertTrue (ITEM_1_2 in duplicates_set)
        self.assertTrue (ITEM_1_3 in duplicates_set)
        self.assertFalse (ITEM_2 in duplicates_set)
    
    def test_adding_item_to_empty_tracker_does_not_create_duplicate(self):

        self._empty_duplicate_tracker.add(NAME_1, ITEM_2)
        self.assertFalse(self._empty_duplicate_tracker.has_duplicates())

    def test_item_is_not_duplicate_in_empty_tracker(self):

        self.assertFalse (self._empty_duplicate_tracker.is_duplicate(NAME_1))
        self.assertTrue (self._empty_duplicate_tracker.is_not_duplicate(NAME_1))
    
    def test_matching_item_is_duplicate_in_single_item_tracker(self):

        self.assertTrue (self._single_item_duplicate_tracker.is_duplicate(NAME_1))
        self.assertFalse (self._single_item_duplicate_tracker.is_not_duplicate(NAME_1))

