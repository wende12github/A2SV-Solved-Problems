# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        resultVisited = set()

        def inorderTraversal(head):
            if not head:
                return False

            if inorderTraversal(head.left):
                return True

            if k - head.val in resultVisited:
                return True
            resultVisited.add(head.val)

            if inorderTraversal(head.right):
                return True

            return False

        return inorderTraversal(root)