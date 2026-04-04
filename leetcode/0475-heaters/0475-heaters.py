class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        result = 0
        houses.sort()
        heaters.sort()

        i = 0
        for h in houses:
            while i < len(heaters) - 1 and heaters[i] <= h:
                i += 1

            left_h = abs(h - (heaters[i-1] if i > 0 else heaters[0]))
            right_h = abs(heaters[i] - h)
            
            result = max(result, min(left_h, right_h))

        return result
