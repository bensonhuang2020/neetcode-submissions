class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        empties = numBottles
        bottles_drank = numBottles
        while empties >= numExchange:
            curr_round = empties // numExchange
            bottles_drank += curr_round
            empties = (empties % numExchange) + curr_round


        return bottles_drank
