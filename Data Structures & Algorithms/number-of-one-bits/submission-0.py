class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)
        res = 0
        for i in binary:
            if i == '1':
                res += 1
        return res