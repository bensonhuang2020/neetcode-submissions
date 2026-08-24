class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        # separate the numbers into buckets
        zeroes = []
        pos = []
        neg = []
        
        # for each relevant number, move them into buckets
        for num in sorted(nums):
            if num < 0:
                neg.append(num)
            elif num > 0:
                pos.append(num)
            else:
                zeroes.append(num)
        
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

        # logic will be repeated, but the simplest way to reason about it is that we perform 2 sum for each positive and negative number. essentially, we flip it, then we look for 2sum in the opposite polarity. the reason we can use 2 pointer is that we have a list of sorted values, we can assume that there's a specific solution to each value or none. essentially, we list[l] + list[r] > target, there is no way that moving l + 1 will let you hit that condition. hence we either find the target and move both, or we move l or r.
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



        
        