# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        self.result_sum = 0

        def traversalEven(root, parentVal, grandparentVal):
            if not root:
                return

            if grandparentVal and grandparentVal.val % 2 == 0:
                self.result_sum += root.val
                
            traversalEven(root.left, root, parentVal)
            traversalEven(root.right, root, parentVal)

        traversalEven(root, None, None)
        return self.result_sum
        