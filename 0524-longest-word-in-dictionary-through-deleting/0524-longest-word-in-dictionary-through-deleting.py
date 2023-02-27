class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def is_valid(string):  # can we get the string by deleting some letters or not
            i = 0
            for letter in s:
                if letter == string[i]:
                    i += 1
                if i == len(string):
                    return True
            return i == len(string)

        dictionary.sort()  # sorting alphabetically
        dictionary.sort(key=len, reverse=True)  # sorting by the length; as a result - sorting both alphabetically and by length
        for word in dictionary:
            if is_valid(word):
                return word
        return ''