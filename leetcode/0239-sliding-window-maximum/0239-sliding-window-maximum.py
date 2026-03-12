class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mono_dequeue = deque()
        result = []

        for i in range(len(nums)):

            if mono_dequeue and mono_dequeue[0] <= i - k:
                mono_dequeue.popleft()

            while mono_dequeue and nums[mono_dequeue[-1]] < nums[i]:
                mono_dequeue.pop()

            mono_dequeue.append(i)

            if i >= k - 1:
                result.append(nums[mono_dequeue[0]])

        return result