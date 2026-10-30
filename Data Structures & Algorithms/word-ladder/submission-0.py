class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # start with either no changes or the endWord is not possible
        if endWord not in wordList or beginWord == endWord:
            return 0

        neigh = collections.defaultdict(list)
        wordList.append(beginWord)
        
        # build the adjacency list
        # the idea is that every word is reachable by the word with a replacement. think how we can represent each word similarly, we just replace each char with a placeholder value and then append into the list.
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                neigh[pattern].append(word)

        # this ensures that we don't go backwards (visited means that we can't visit it again)
        visit = set([beginWord])
        q = deque([beginWord])
        res = 1
        # the res starts with 1 since it means that we need a single transformation (we already dealt with the case where the start word is the end word). after that, we recreate the pattern to find what goes next in the bfs loop. this should be any of the words in the queue, we go through each character to access their dictionary values to find the "next" word. this goes back in the queue, and at last we increase the res value. if we ever find the endWord in the queue, that means that we traveled enough to find it and we're done. if we never find the endWord, it's not connected in the graph.
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neighbor_word in neigh[pattern]:
                        if neighbor_word not in visit:
                            visit.add(neighbor_word)
                            q.append(neighbor_word)
            res += 1
        return 0