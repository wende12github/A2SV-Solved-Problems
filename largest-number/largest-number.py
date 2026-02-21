class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not nums:
            return "0"
            
        strs = [str(x) for x in nums]
        
        def compare(a: str, b: str) -> int:
            ab = a + b
            ba = b + a
            if ab > ba: return -1
            if ab < ba: return  1
            return 0
        
        strs.sort(key=cmp_to_key(compare))
        
        if strs[0] == "0":
            return "0"
            
        return "".join(strs)
