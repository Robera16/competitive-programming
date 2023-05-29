# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def pre(root):
            if root is None:
                return ''
            x=str(root.val)
            lt='('+pre(root.left)+')'
            rt='('+pre(root.right)+')'
            if lt=='()' and rt=="()":
                return x
            if rt=='()':
                return x+lt
            return x+lt+rt
        s=pre(root)
        return s