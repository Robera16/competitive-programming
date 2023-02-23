class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        n = len(box)
        m = len(box[0])
        
        result = [['.'] * n for i in range(m)]

        for i in range(n):
            slow = m - 1
            for fast in range(m - 1, -1, -1):
                if box[i][fast] == '#':
                    result[slow][n - i - 1] = '#'
                    slow -= 1
                elif box[i][fast] == '*':
                    result[fast][n - i - 1] = '*'
                    slow = fast - 1
        
        return result