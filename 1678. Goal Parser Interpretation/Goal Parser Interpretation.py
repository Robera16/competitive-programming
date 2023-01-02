class Solution:
    def interpret(self, command: str) -> str:
        stack=[command[0]]
        for indx in range(1, len(command)):
            if stack[-1]=='(' and command[indx]==')':
                stack.pop()
                stack.append('o')
            elif stack[-1]=='l' and command[indx]==')':
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append('al')
            else:
                stack.append(command[indx])
      
        return ''.join(stack)