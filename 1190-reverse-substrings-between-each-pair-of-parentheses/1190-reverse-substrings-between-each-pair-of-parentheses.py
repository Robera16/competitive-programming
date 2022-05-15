class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        output = ''
        result = ''
        for char in s:
            if char != ")":
                stack.append(char)
            else:
                stack_char = stack.pop()
                while stack_char != "(":
                    output += stack_char
                    stack_char = stack.pop()
                for letter in output:
                    stack.append(letter)
            output = ''
        for char in stack:
            result+=char
        return result