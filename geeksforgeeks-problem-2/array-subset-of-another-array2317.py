class Solution:
    def isSubset(self, a, b):
        counter = {}
        for num in a:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] =1
  
        for num in b:
            if num not in counter or counter[num] == 0:
                return False
            counter[num] -= 1
        return True
