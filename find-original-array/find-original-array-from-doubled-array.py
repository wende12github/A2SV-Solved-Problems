class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        counter = Counter(changed)
        original = []
        
        if len(changed) % 2:
            return original

        changed.sort()

        for num in changed:
            if counter[num] == 0:
                continue
            else:
                if counter.get(2 * num, 0) >= 1:
                    original.append(num)
                    counter[2 * num] -= 1
                    counter[num] -= 1
                else:
                    return []

        return original
