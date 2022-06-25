class Solution(object):
    def removeKdigits(self, num, k):
        if k==len(list(num)):
            return "0"
        stack=[]
        for val in num:
            if not len(stack):
                stack.append(val)
            else:
                if k:
                    if stack[-1] <= val:
                        stack.append(val)
                    else:
                        while(len(stack) and k and (stack[-1] > val)):
                            stack.pop()
                            k-=1
                        stack.append(val)
                else:
                    stack.append(val)
        while(k):
            stack.pop()
            k-=1
        while(len(stack) >1 and stack[0]=='0'):
            stack.pop(0)
       
        answer=''
        for val in stack:
            answer+=val
        return answer
        """
        :type num: str
        :type k: int
        :rtype: str
        """