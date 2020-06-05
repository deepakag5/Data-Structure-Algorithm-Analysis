from random import choice


class RandomizedSet:

    def __init__(self):
        self.list = []
        self.dict = {}

    def insert(self, val):
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def delete(self, val):
        if val in self.dict:
            last_element, idx = self.list[-1], self.dict[val]
            self.list[idx], self.dict[last_element] = last_element, idx
            self.list.pop()
            del self.dict[val]
            return True
        return False

    def getRandom(self):
        return choice(self.list)
