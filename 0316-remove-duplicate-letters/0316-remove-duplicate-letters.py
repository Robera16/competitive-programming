class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        # monotonically increasing
        # but before poping check that if there is at least one instance to the right of the current pointer position on s
        # only one character inserted
        counter = Counter(s)
        stack=[]
        track = set()
        for char in s:
            if char not in track:
                while stack and stack[-1] >= char:
                    if counter[stack[-1]]: # track if another instance found
                        track.remove(stack.pop())
                    else:
                        break

                stack.append(char)
                track.add(char)
                
            counter[char]-=1
                
        return ''.join(stack)