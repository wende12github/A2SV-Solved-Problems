# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        def helperRec(left, right):
            if left > right:
                return None

            m = left
            for i in range(left + 1, right + 1):
                if nums[i] > nums[m]:
                    m = i
            
            node = TreeNode(nums[m])
            node.left = helperRec(left, m - 1)
            node.right = helperRec(m + 1, right)
            
            return node
        return helperRec(0, len(nums) - 1)
