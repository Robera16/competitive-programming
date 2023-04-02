# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
               
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def minValueNode(node):
            current = node
            while current.left is not None:
                current = current.left
            return current 
        
        if not root:
            return root
        else:
            if key < root.val:
                root.left = self.deleteNode(root.left, key)
            elif key > root.val:
                root.right = self.deleteNode(root.right, key)
            else:
                if not root.left:
                    temp = root.right
                    root = None
                    return temp
                elif not root.right:
                    temp = root.left
                    root = None
                    return temp
                else:
                    temp = minValueNode(root.right)
                    root.val = temp.val
                    root.right = self.deleteNode(root.right, temp.val)
                    
        return root