class TrieNode:

    def __init__(self):
        self.children = [None] * 26
        self.isComplete = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            distance = ord(char) - ord('a')
            if cur.children[distance] == None:
                cur.children[distance] = TrieNode()
            cur = cur.children[distance]
        cur.isComplete = True


    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            distance = ord(char) - ord('a')
            if cur.children[distance] == None:
                return False
            cur = cur.children[distance]
        return cur.isComplete
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            distance = ord(char) - ord('a')
            if cur.children[distance] == None:
                return False
            cur = cur.children[distance]
        return True
        