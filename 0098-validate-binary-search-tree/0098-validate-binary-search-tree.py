class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def valid(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return valid(node.left, low, node.val) and valid(node.right, node.val, high)
        
        return valid(root, -inf, inf)