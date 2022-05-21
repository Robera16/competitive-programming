class Solution:
    def decodeString(self, s: str) -> str:
        
        string = num = ""
        stack = []
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                while stack[-1] != '[':
                    string += stack.pop()
                stack.pop()
                string = string[::-1]
                while len(stack) and stack[-1].isdigit():
                    num += stack.pop()
                num = int(num[::-1])
                for i in range(num):
                    for c in string:
                        stack.append(c)
                string = num = ""
          
        for c in stack:
            string += c
        return string