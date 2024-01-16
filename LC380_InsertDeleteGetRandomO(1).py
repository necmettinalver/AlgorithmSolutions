from random import choice

class RandomizedSet:

    def __init__(self):
        self.list_key : list = []
        self.dict_id : dict = {}

    def insert(self, val: int) -> bool:
        if val in self.dict_id:
            return False
        
        self.list_key.append(val)
        self.dict_id[val] = len(self.list_key)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict_id:
            return False

        last_key = self.list_key[-1]
        id_val = self.dict_id[val]
        self.dict_id[last_key] = id_val
        self.list_key[id_val] = last_key
        self.list_key.pop()
        del self.dict_id[val]
        return True

    def getRandom(self) -> int:
        return choice(self.list_key)