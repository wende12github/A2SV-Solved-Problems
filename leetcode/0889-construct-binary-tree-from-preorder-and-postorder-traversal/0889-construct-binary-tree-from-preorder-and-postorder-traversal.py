# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(postorder)
        map_val_indx = {}

        for indx, val in enumerate(postorder):
            map_val_indx[val] = indx

        def helperRec(l1, l2, indx):
            if l1 > l2:
                return None
            
            root = TreeNode(preorder[l1])
            if l1 != l2:
                left_val = preorder[l1 + 1]
                m = map_val_indx[left_val]
                left_s = m - indx + 1
                
                root.left = helperRec(l1 + 1, l1 + left_s, indx)
                root.right = helperRec(l1 + left_s + 1, l2, m + 1)

            return root

        return helperRec(0, n - 1, 0)
