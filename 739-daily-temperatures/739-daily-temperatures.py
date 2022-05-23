class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        output=[]
        output.append(0)
        stack.append(len(temperatures)-1)
        i=len(temperatures)-2
        while i>=0:
            if temperatures[i] < temperatures[stack[-1]]:
                val=stack[-1]-i
            else:
                while temperatures[i] >= temperatures[stack[-1]]:
                    stack.pop()
                    if not len(stack):
                        val=0
                        break
                
                if len(stack):
                    val=stack[-1]-i
                else:
                    val=0
            stack.append(i)
            output.append( val)
            i-=1
        output=output[::-1]
        return output