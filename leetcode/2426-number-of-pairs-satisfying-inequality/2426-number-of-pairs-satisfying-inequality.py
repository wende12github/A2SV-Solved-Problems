class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        l = SortedList()
        result = 0
        for n1,n2 in zip(nums1, nums2):
            result += l.bisect_right(n1 - n2 + diff)
            l.add(n1 - n2)

        return result