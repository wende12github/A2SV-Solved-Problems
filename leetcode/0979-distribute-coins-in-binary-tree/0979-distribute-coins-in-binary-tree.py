# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.result = 0

        def dfsBacktrack(head):
            if not head:
                return [0, 0]

            left_size, left_coin = dfsBacktrack(head.left)
            right_size, right_coin = dfsBacktrack(head.right)

            balance = 1 + left_size + right_size
            total_coin = head.val + left_coin + right_coin

            self.result += abs(balance - total_coin)

            return [balance, total_coin]

        dfsBacktrack(root)
        return self.result