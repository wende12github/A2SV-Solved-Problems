# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root == None:
            return 0

        return self.pathSum(root.left, targetSum) + self.pathSumHelper(root, targetSum) + self.pathSum(root.right, targetSum)

    def pathSumHelper(self, root, targetSum):
        if root == None:
            return 0

        result = 0
        if root.val == targetSum:
            result += 1
        result += self.pathSumHelper(root.left, targetSum - root.val)
        result += self.pathSumHelper(root.right, targetSum - root.val)

        return result