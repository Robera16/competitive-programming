# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        res = []
        
        def inorderTraverse(root):
            if not root:
                return
            inorderTraverse(root.left)
            res.append(root.val)
            inorderTraverse(root.right)
        
        inorderTraverse(root)
        i=0
        min_val=float(inf)
        while i < len(res)-1:
            if res[i+1] - res[i] < min_val:
                min_val = res[i+1] - res[i]
            i+=1
        return min_val