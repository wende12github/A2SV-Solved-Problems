class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        counter = defaultdict(int)

        result = 0
        slow = fast = 0

        for r in range(len(nums)):
            counter[nums[r]] += 1

            while len(counter) > k:
                counter[nums[fast]] -= 1

                if counter[nums[fast]] == 0:
                    counter.pop(nums[fast])
                fast += 1
                slow = fast

            while counter[nums[fast]] > 1:
                counter[nums[fast]] -= 1
                fast += 1

            if len(counter) == k:
                result += fast - slow + 1

        return result
