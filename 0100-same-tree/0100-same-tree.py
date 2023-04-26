# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        output_p = []
        output_q = []
        
        def inorderTraversal(root, output, c):
            if not root:
                return
            inorderTraversal(root.left, output, c+1)
            output.append([root.val, c])
            inorderTraversal(root.right, output, c+1)
            
        inorderTraversal(p, output_p, 0)
        inorderTraversal(q, output_q, 0)
        
        return output_p==output_q
        