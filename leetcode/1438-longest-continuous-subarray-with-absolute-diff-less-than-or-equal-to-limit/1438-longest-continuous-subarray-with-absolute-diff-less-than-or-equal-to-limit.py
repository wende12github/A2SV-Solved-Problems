class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxDeque = deque()
        minDeque = deque()

        left = 0
        result = 0

        for right in range(len(nums)):

            while maxDeque and nums[right] > maxDeque[-1]:
                maxDeque.pop()
            maxDeque.append(nums[right])

            while minDeque and nums[right] < minDeque[-1]:
                minDeque.pop()
            minDeque.append(nums[right])

            while maxDeque[0] - minDeque[0] > limit:

                if nums[left] == maxDeque[0]:
                    maxDeque.popleft()

                if nums[left] == minDeque[0]:
                    minDeque.popleft()

                left += 1

            result = max(result, right - left + 1)

        return result