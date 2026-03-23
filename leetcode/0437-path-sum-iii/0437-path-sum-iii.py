# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.pathCount = 0
        self.pathSums = {0: 1}

        def dfsHelper(root, currentSum):
            if root is None:
                return

            currentSum += root.val
            self.pathCount += self.pathSums.get(currentSum - targetSum, 0)
            self.pathSums[currentSum] = self.pathSums.get(currentSum, 0) + 1

            if root.right:
                dfsHelper(root.right, currentSum)
            if root.left:
                dfsHelper(root.left, currentSum)

            self.pathSums[currentSum] -= 1
            
        dfsHelper(root, 0)
        return self.pathCount