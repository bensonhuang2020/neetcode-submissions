class Solution:
    def checkValidString(self, s: str) -> bool:
        # the most nasty naive approach would be to recursively attempt for every posssible version of * and return.

        # what if we kept track of both left parentheses and stars?
        left_parentheses = []
        stars = []

        # we can iterate through the string and if we find a star or a left parenthesis, we can append to the running lists. note, since we have 2 lists, we only need the indices
        for i in range(len(s)):
            if s[i] == "(":
                left_parentheses.append(i)
            elif s[i] == "*":
                stars.append(i)
            else:
                # if we hit a right parenthesis, we try to remove the lefts cause they're less flexible. however, if we're out of rights, we have to remove the stars. if there's none in either, we fail out.
                if left_parentheses:
                    left_parentheses.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
            # at the end, if the number of stars is greater or equal to the number of lefts, we can negate the lefts with rights and then empty string the rest. however, what happens if the lefts come AFTER the stars?
            # hence, let's iterate while we have both stars and lefts. if off the top, stars is less than left_parentheses, that means we can't match. we gotta match all of the lefts or it's false. at the end, if left is not empty but stars is, it's false.
        while stars and left_parentheses:
            if stars[-1] > left_parentheses[-1]:
                stars.pop()
                left_parentheses.pop()
            else:
                return False

        return len(left_parentheses) == 0

