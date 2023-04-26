# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        q = deque()
        q.append([root, 0, 0])  
        res, output=[], []
        while q:
            for i in range(len(q)):
                temproot, row, col = q.popleft()
                res.append([temproot.val, row, col])
                
                if temproot.left:
                    q.append([temproot.left, row+1, col-1])
                if temproot.right:
                    q.append([temproot.right, row+1, col+1])
        
        
        def custom_key(sublist):
            return (sublist[2], sublist[1], sublist[0])

        res.sort(key=custom_key)
        output.append([res[0][0]])
        prev=res[0][2]
     
        for i in range(1, len(res)):
            if res[i][2]==prev:
                output[-1].append(res[i][0])
            else:
                output.append([res[i][0]])
            prev=res[i][2]
        
        return output