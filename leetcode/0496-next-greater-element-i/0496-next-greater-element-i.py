class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []

        result = defaultdict(lambda: -1)
        answer = []
        for num in nums2:
            
            while stack and stack[-1] < num:
                result[stack[-1]] = num
                stack.pop()

            stack.append(num)
            
        for num in nums1:
            answer.append(result[num])

        return answer