class Solution:
    def findComplement(self, num: int) -> int:
        binary_string = bin(num)
        output = ''
        for char in binary_string[2:]:
            output+='0' if char=='1' else '1'
        return int(output, 2)
        