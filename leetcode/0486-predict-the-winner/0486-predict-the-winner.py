class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        visited = defaultdict(int)
        def predictWinner(left, right, turn):
            if left > right:
                return 0
            
            if (left, right, turn) in visited:
                return visited[(left, right, turn)]

            result = 0
            if turn == 0:
                result = max(nums[left] + predictWinner(left + 1, right, 1), nums[right] + predictWinner(left, right - 1, 1))
            else:
                result = min(predictWinner(left + 1, right, 0), predictWinner(left, right - 1, 0))

            visited[(left, right, turn)] = result
            return result

        p1_scores = predictWinner(0, len(nums)-1, 0)
        p2_scores = predictWinner(0, len(nums)-1, 1)

        return p1_scores >= p2_scores