# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        levels = []
        level = 0
        queue = deque([(root, level)])
        currLevel = []
        output = []
        
        while queue:
            node, nodeLevel = queue.popleft()

            if not node:
                continue

            if nodeLevel != level:
                levels.append(currLevel.copy())
                level += 1
                currLevel = []

            currLevel.append(node.val)
            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))

        if currLevel:
            levels.append(currLevel.copy())
    
        for ele in levels:
            output.append(sum(ele)/len(ele))
            
        return output

        