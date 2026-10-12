class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carries = False

        # essentially, we iterate backwards. keep track of whether we carry over or not. if we do, we keep going right to left and increment. if we stop carrying or don't carry at all, we break and just finish. if we go through the entire loop and turn everything into 0's, this means that the left most number is now a 1, so we must insert a 1. time complexity is O(n) since we go through the whole list, O(1) for space since we don't make anything other than constants.
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
                carries = True
            else:
                digits[i] += 1
                carries = False
            
            if not carries:
                break
        if carries:
            digits.insert(0, 1)
        return digits
