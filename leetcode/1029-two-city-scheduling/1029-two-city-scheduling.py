class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        cost_a = 0
        for costA, costB in costs:
            cost_a += costA

        diff = []

        for costA, costB in costs:
            diff.append(costB - costA)

        diff.sort()

        cost_b = 0
        for i in range(len(costs)//2):
            cost_b += diff[i]

        return cost_a + cost_b