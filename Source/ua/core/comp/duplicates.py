class DuplicateTracker:
    
    def __init__(self):
        self._item_dict = {}
        self._duplicates_dict = {}
    
    def add (self, name, item):

        if self.is_not_duplicate(name):    
            self._item_dict[name] = item
        else:
            if name not in self._duplicates_dict:
                duplicate_items = [self._item_dict[name]]
                self._duplicates_dict[name] = duplicate_items
            else:
                duplicate_items = self._duplicates_dict[name]
            
            duplicate_items.append(item)
    
    def duplicates_dict(self):
        return self._duplicates_dict
                
    def is_duplicate (self, name):
        return name in self._item_dict

    def is_not_duplicate (self, name):
        return not self.is_duplicate(name)

    def has_duplicates(self):
        return len(self._duplicates_dict) > 0