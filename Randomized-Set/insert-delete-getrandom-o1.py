class RandomizedSet:

    def __init__(self):
        self.rand_list = []
        self.idx_map = {}

    def insert(self, val: int) -> bool:
        if val in self.idx_map:
            return False

        self.rand_list.append(val)
        self.idx_map[val] = len(self.rand_list) - 1
        
        return True

    def remove(self, val: int) -> bool:
        if not val in self.idx_map:
            return False
        
        idx = self.idx_map[val]
        self.rand_list[idx] = self.rand_list[-1]

        self.idx_map[self.rand_list[-1]] = idx
        self.rand_list.pop()

        del self.idx_map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.rand_list)
        
