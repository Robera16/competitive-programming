# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        q = deque()
        q.append([root, 1])
        max_width = 0
        
        while q:
            
            _, first_col = q[0]
            _, last_col = q[-1]
            
            max_width = max(max_width, last_col - first_col + 1)
            
            for i in range(len(q)):
                temproot, col = q.popleft()
                if temproot.left:
                    q.append([temproot.left, col*2])
                if temproot.right:
                    q.append([temproot.right, col*2 + 1])
        
        return max_width