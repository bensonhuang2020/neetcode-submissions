class Solution:
    def countBits(self, n: int) -> List[int]:
        # the most inefficient way would be to create an empty list, and do a for loop to the range of n. and then for each one, we do the bit manipulation.
        res = []
        for num in range(n + 1):
            ones = 0
            while num:
                ones += num & 1
                num = num >> 1
            res.append(ones)
        return res
