class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        # separate the numbers into buckets
        zeroes = []
        pos = []
        neg = []
        
        # for each relevant number, move them into buckets
        for num in nums:
            if num < 0:
                neg.append(num)
            elif num > 0:
                pos.append(num)
            else:
                zeroes.append(num)

        pos = sorted(pos)
        neg = sorted(neg)
        
        # handle the 0, 0, 0 case first, then the -x, 0, x cases
        pos_set = set(pos)
        neg_set = set(neg)
        if zeroes:
            if len(zeroes) > 2:
                res.append([0, 0, 0])
            for i in pos_set:
                if -i in neg_set:
                    res.append([-i, 0, i])
        
        # now let's handle the [-, -, +] cases
        for posi in pos_set:
            target = -posi
            l, r = 0, len(neg) - 1

            while l < r:
                added = neg[r] + neg[l]
                if added == target:
                    proposed_sum = [neg[l], neg[r], posi]
                    if proposed_sum not in res:
                        res.append(proposed_sum)
                    r -= 1
                    l += 1
                elif added < target:
                    l += 1
                else:
                    r -= 1

        # now let's handle the [-, +, +] cases
        for negi in neg_set:
            target = -negi
            l, r = 0, len(pos) - 1

            while l < r:
                added = pos[r] + pos[l]
                if added == target:
                    proposed_sum = [negi, pos[l], pos[r]]
                    if proposed_sum not in res:
                        res.append(proposed_sum)
                    r -= 1
                    l += 1
                elif added < target:
                    l += 1
                else:
                    r -= 1
        
        return list(res)



        
        