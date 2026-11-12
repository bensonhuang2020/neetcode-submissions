class Solution:
    def reorganizeString(self, s: str) -> str:
        strings = Counter(s)
        res = ""
        hp = []
        for key, val in strings.items():
            heapq.heappush(hp, (-val, key))
        prev = None
        while hp or prev:
            # this means that we have nothing else in the maxHeap except for the prev, which means that we have a dupe. we've exhausetd everything else.
            if prev and not hp:
                return ""

            count, char = heapq.heappop(hp)
            res += char
            count += 1

            # we're holding the previous so we're adding it back to the maxheap so it can get added in again.
            if prev:
                heapq.heappush(hp, prev)
                prev = None
            # if count is not 0, we set it to prev so that we can add it in next time. if it's 0, we don't have to worry about it being found again.
            if count != 0:
                prev = (count, char)
        
        return res
        # time is O(nlogn) since heap push and pop n elements with logn. 
        # space is also O(n) since we store all the elements.