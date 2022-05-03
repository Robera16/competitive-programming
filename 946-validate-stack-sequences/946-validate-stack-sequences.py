class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
       
        stack=[]
        for i in pushed:
            stack.append(i)
            
            while stack[-1]==popped[0]:
                stack.pop()
                popped.pop(0)
                if not len(stack):
                    break
        
        if len(stack)==0:
            return True
        else:
            return False