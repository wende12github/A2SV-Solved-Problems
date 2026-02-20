class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        resualt = 0
        max_val = max(piles)
        count = [0] * (max_val + 1)

        for i in piles:
            count[i] += 1

        chance = len(piles)/3
        turn = 1
        while chance != 0:
            if count[max_val] > 0:
                if turn == 1:
                    turn = 0
                else:
                    chance -= 1
                    turn = 1
                    resualt += max_val
                count[max_val] -= 1
            else:
                max_val -= 1        

        return resualt
