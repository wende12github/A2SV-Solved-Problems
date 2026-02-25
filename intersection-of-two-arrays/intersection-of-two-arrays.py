class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    if nums1[i] in result:
                        continue
                    result.append(nums1[i])
                
        return result
