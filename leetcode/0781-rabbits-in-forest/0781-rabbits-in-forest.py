class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter = Counter(answers)
        result = 0

        for key, count in counter.items():

            group = key + 1
            groups = (count + group - 1) // group

            result += groups * group

        return result