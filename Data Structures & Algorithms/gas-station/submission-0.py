class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # the naïve solution would be to calculate the amount of cost per each starting station by doing the whole loop around. what if we just did the max value for starting where we find the greatest value. this would always be the only starting point. however, who's to say that the next stations aren't worse off? 

        # if the sum of gas is less than sum of cost, then we obviously can't finish since there's no gas combination that can finish the trip
        if sum(gas) < sum(cost):
            return -1
        # for each station, we keep a total running until we hit negative. if we hit negative, we go ahead of where we stopped anyways.
        # essentially, if we ever hit negative, we know we couldnt' have done it there anyways. essentially, if we had negative, every number we passed would fail. we also know that it has to pass at some point cause the differences are positive.
        total = 0
        res = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                res = i + 1
        return res



