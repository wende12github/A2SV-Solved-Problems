class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        MOD = 10**9 + 7
        frq = {}
        sorted_list = []
        result = 0
        
        for num in instructions:
            indx = bisect.bisect_right(sorted_list, num)
            
            cnt_smaller = bisect.bisect_left(sorted_list, num)
            cnt_larger = len(sorted_list) - indx
            
            result = (result + min(cnt_smaller, cnt_larger)) % MOD
            
            bisect.insort(sorted_list, num)
            
        return result
