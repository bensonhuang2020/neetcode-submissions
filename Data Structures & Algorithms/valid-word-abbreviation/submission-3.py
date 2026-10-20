class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # word index, abbreviation index
        # this is just array/string manipulation
        wi = ai = 0
        while wi < len(word) and ai < len(abbr):
            if word[wi] == abbr[ai]:
                wi += 1
                ai += 1
            # this is potentially a running number
            elif abbr[ai].isnumeric():
                # no leading 0's
                if abbr[ai] == '0':
                    return False
                curr_num = abbr[ai]
                ai += 1
                while ai < len(abbr) and abbr[ai].isnumeric():
                    curr_num += abbr[ai]
                    ai += 1
                wi += int(curr_num)
            else:
                return False

        return wi == len(word) and ai == len(abbr)

        # time complexity is O(n) since we potentially just go through every string, although pendantically it's O(max(len(word), len(abbr)))
        # space is just O(1), everything is constant, jsut variables