class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # i'm gonna iterate through the string s and mark where we find each last.
        locations = {}
        # enumerate gives us the tuple of (index, char)
        for i, c in enumerate(s):
            locations[c] = i
        
        res = []
        # initial size is 0, the end of the first substring is 0 too.
        size = end = 0
        # going through the list again, we look for index and char. each char gets size of 1. end gets reassigned to the last location we found the char. this will keep going right if subsequent chars in the partition are found further in the array. if we reach the end (meaning that we found the end of the partition), we restart
        for i, c in enumerate(s):
            # assume that the starting partition starts at the beginning
            size += 1
            end = max(end, locations[c])

            if i == end:
                res.append(size)
                size = 0

        return res
    # time complexity is O(2n) -> O(n) since we loop through the array 2x. 
    # space complexity is O(n) since we're holding the chars in 1 dict. Actually, could it be O(1) since we're only working with chars and there's only 26 lowercase?


