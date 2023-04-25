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
        q.append((root,1))
        maxwidth = 0
        while q:
            level_length = len(q)
            _, last_column = q[-1]
            _, first_column = q[0]
            
            maxwidth = max(maxwidth, last_column-first_column+1)
            
            for _ in range(level_length):
                tmproot,column = q.popleft()
                if tmproot.left:
                    q.append((tmproot.left, column*2))
                if tmproot.right:
                    q.append((tmproot.right, column*2+1))
            
        return maxwidth