class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        result = []
        left = 0
        curr_W = deque()
        curr_negativeNums = SortedList()
        
        for right in range(n):
            num = nums[right]
            curr_W.append(num)
            if num < 0:
                curr_negativeNums.add(num)

            if right - left + 1 > k:
                removedNum = curr_W.popleft()
                if removedNum < 0:
                    curr_negativeNums.remove(removedNum)
                left += 1

            if right - left + 1 == k:
                if len(curr_negativeNums) < x:
                    result.append(0)
                else:
                    result.append(curr_negativeNums[x - 1])
        
        return result