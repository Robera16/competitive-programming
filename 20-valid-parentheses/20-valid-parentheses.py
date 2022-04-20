class Solution:
    def isValid(self, s: str) -> bool:
        dict={
            '}':'{',
            ')':'(',
            ']':'['    
        }
        opening=['{', '(', '[']
        stack=[]
        ls=list(s)
        
        for c in ls:
            if opening.count(c):
                stack.append(c)
            else:
                if len(stack)==0:
                    return False
                if stack[-1]==dict[c]:
                    stack.pop()
                else:
                    return False
                
        if len(stack)!=0:
            return False
        return True