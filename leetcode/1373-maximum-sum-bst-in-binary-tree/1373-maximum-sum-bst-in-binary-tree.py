# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        result = [0]

        def dfsRec(node):
            if not node:
                return True, float('inf'), float('-inf'), 0

            l_isBST, left_min, left_max, left_sum = dfsRec(node.left)
            r_isBST, right_min, right_max, right_sum = dfsRec(node.right)

            if l_isBST and r_isBST and left_max < node.val and right_min > node.val:

                current_sum = left_sum + node.val + right_sum
                result[0] = max(result[0], current_sum)
                
                return True, min(left_min, node.val), max(right_max, node.val), current_sum

            return False, float('-inf'), float('inf'), 0

        dfsRec(root)
        return result[0]