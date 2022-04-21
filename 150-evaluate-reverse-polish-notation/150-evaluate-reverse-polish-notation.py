class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        
        op1=0;
        op2=0
        stack=[]
        operators=['+', '-', '*', '/']
        result=0
        if len(tokens)==1:
            return int(tokens[0])
        for i in tokens:
            if operators.count(i):
                
                if i=='+':
                    result=stack.pop()+stack.pop()
                elif i=='-':
                    op1=stack.pop()
                    op2=stack.pop()
                    result=op2-op1
                elif i=='*':
                    result=stack.pop()*stack.pop()
                elif i=="/":
                    op1=stack.pop()
                    op2=stack.pop()
                    if(abs(op1) > abs(op2)):
                        result=0
                    else:
                        result=trunc(op2/op1)
                    
                     
                stack.append(result)
                
            else:
                stack.append(int(i))
        
        return result