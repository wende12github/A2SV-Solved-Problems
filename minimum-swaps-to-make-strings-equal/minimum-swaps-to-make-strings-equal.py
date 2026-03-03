class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy_count = 0
        yx_count = 0

        for char1, char2 in zip(s1, s2):
            if char1 != char2:
                if char1 == 'x': 
                    xy_count += 1
                else: 
                    yx_count += 1
        
        if (xy_count + yx_count) % 2 == 1: 
            return -1
        
        return (xy_count // 2) + (yx_count // 2) + (2 if xy_count % 2 == 1 else 0)
