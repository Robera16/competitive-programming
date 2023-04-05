# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        output = []
        def traverse(node, s):
            if s!='':
                s+='->'
            s+=str(node.val)
            if not node.left and not node.right:
                output.append(s)
            else:
                if node.left:
                    traverse(node.left, s)
                if node.right:
                    traverse(node.right, s)
        
        traverse(root, '')
        return output
                
                
                
            