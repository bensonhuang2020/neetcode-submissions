class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # pretty simple, but for each of the numExchange drank, we get a bottle back until we don't have any bottles left. easier to understand too cause after we drink all of the start ones, we have 0 left.
        drunk = numBottles
        while numExchange <= numBottles:
            numBottles -= numExchange
            numBottles += 1
            drunk += 1

        return drunk
