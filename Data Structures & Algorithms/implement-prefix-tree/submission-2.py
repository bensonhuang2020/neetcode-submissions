class TrieNode:

    def __init__(self):
        # a trie has children to represent the tree-liek structure. in this case with the autocompletion, there are 26 possible characters. the initial root value can tell you a lot, but it starts with nothing.
        self.children = [None] * 26
        self.isComplete = False

class PrefixTree:

    def __init__(self):
        # init just gives you a root with no value
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        # for insert, we're just creating a new child node every time we travese the insertion, but if it already exists, we don't do anything. then, at the end of the word, we want to just set the boolean that the word is complete (anything works here, there's no defined definition)
        cur = self.root
        for char in word:
            distance = ord(char) - ord('a')
            if cur.children[distance] == None:
                cur.children[distance] = TrieNode()
            cur = cur.children[distance]
        cur.isComplete = True


    def search(self, word: str) -> bool:
        # the search then traverses the tree the same exact way an insertion does it, but at the end, we just want to check that the boolean is correct.
        cur = self.root
        for char in word:
            distance = ord(char) - ord('a')
            if cur.children[distance] == None:
                return False
            cur = cur.children[distance]
        return cur.isComplete
        

    def startsWith(self, prefix: str) -> bool:
        # here, same as search but we don't care if the boolean is correct, only that we can fully traverse.
        cur = self.root
        for char in prefix:
            distance = ord(char) - ord('a')
            if cur.children[distance] == None:
                return False
            cur = cur.children[distance]
        return True
        