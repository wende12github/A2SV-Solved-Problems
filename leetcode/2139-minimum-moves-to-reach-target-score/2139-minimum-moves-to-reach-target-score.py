class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count_op = 0

        # if target == 1:
        #     return count_op

        while target > 1 and maxDoubles:
            if target == 1:
                return count_op

            if target % 2 == 0:
                target //= 2
                maxDoubles -= 1
            else:
                target -= 1

            count_op += 1

        if target > 1:
            count_op += (target - 1)
            
        return count_op