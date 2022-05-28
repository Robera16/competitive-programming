class Solution:
    def compress(self, chars: List[str]) -> int:
        counter=1
        stack=[chars[0]]
        for i in range(1, len(chars)):
            if stack[-1]==chars[i]:
                counter+=1
            else:
                if counter!=1:
                    stack.extend(list(str(counter)))
                stack.append(chars[i])
                counter=1
        if counter!=1:
            stack.extend(list(str(counter)))
        
        chars.clear()
        chars.extend(stack)
        return len(chars)