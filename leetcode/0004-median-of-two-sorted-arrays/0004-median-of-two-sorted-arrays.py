class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merg = sorted(nums1 + nums2)

        left = 0
        right = len(merg) - 1
        mid = (left + right) // 2
        
        if len(merg) % 2 != 0:
            return float(merg[mid])
        else:
            midd = (merg[mid] + merg[mid + 1]) / 2.0

        return midd