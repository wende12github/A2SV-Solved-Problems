import bisect
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        result = []
        sort_num = []

        for n in reversed(nums):
            m = bisect.bisect_left(sort_num, n)
            result.append(m)

            bisect.insort(sort_num, n)

        return result[::-1]