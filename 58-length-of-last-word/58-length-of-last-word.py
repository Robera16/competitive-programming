class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_list = s.split()
        count = 0
        for ch in word_list.pop():
            count+=1
        return count