class WordDictionary:

    def __init__(self):
        self.root = dict()

    def addWord(self, word: str) -> None:
        node = self.root
        for w in word:
            if w not in node:
                node[w] = dict()
            node = node[w]
        node['#'] = ''

    def search(self, word: str) -> bool:
        def dfs(word , start , node):
            if word == '' and '#' in node:
                return True
            if len(word) > 0 and node == '':
                return False
            
            for index in range(start, len(word)):
                w = word[index]
                if w != '.' and w not in node:
                    return False
                elif w in node:
                    node = node[w]
                elif w == '.':
                    for j in node.keys():
                        if dfs(word,index+1,node[j]):
                            return True
                    return False
            if '#' in node:
                return True
            return False
        return dfs(word ,0 , self.root )