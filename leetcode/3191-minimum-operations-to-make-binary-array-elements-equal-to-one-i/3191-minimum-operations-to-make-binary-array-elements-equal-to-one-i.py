class Solution:
    def minOperations(self, nums: List[int]) -> int:
        length = len(nums)
        queue = deque()
        mini_ops = 0

        for i in range(length):

            while queue and queue[0] < i:
                queue.popleft()

            flips = len(queue) % 2
            current = nums[i] ^ flips

            if current == 0:
                if i + 2 >= length:
                    return -1

                mini_ops += 1
                queue.append(i + 2)

        return mini_ops