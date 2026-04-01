# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = [root.val]

        def dfsRec(node):
            if not node:
                return 0
        
            l_max = max(dfsRec(node.left), 0)
            r_max = max(dfsRec(node.right), 0)

            current = node.val + l_max + r_max
            result[0] = max(result[0], current)

            return node.val + max(l_max, r_max)

        dfsRec(root)
        return result[0]