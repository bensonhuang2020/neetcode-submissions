class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isComplete = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            i = ord(c) - ord('a')
            if cur.children[i] == None:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        cur.isComplete = True
        

    def search(self, word: str) -> bool:
        def dfs(ind, cur):
            if ind == len(word):
                return cur.isComplete

            ch = word[ind]

            if ch == '.':
                # Try every possible next character
                for child in cur.children:
                    if child is not None and dfs(ind + 1, child):
                        return True
                return False

            i = ord(ch) - ord('a')

            if cur.children[i] is None:
                return False

            return dfs(ind + 1, cur.children[i])
            
        return dfs(0, self.root)
