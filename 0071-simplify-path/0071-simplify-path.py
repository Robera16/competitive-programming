class Solution:
    def simplifyPath(self, path: str) -> str:
        split_path = path.split('/')
        stack = []
        
        for folder in split_path:
            if folder == '..':
                if stack:
                    stack.pop()
            elif folder == '.' or not folder:
                continue
            else:
                stack.append(folder)
        
        return '/'+'/'.join(stack)