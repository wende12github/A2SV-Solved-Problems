# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
    
        def dfs(node):
            if not node:
                return [0, 0]
            
            if node in memo:
                return memo[node]
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            rob_curr = node.val + left[1] + right[1]
            skip_curr = max(left[0], left[1]) + max(right[0], right[1])
            
            memo[node] = [rob_curr, skip_curr]
            return memo[node]

        return max(dfs(root))