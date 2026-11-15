class StockSpanner:

    def __init__(self):
        self.stockSpanner = []

    def next(self, price: int) -> int:
        # we actually can use a monotonic decreasing stack since it'll reset. essentially, if we're larger than the itme on the top, we're larger than anything it's larger than. keep popping until we can't.
        span = 1
        while self.stockSpanner and self.stockSpanner[-1][0] <= price:
            span += self.stockSpanner[-1][1]
            self.stockSpanner.pop()
        self.stockSpanner.append((price, span))
        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)