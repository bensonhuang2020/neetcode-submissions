class StockSpanner:

    def __init__(self):
        self.stockSpanner = []
        self.size = 0

    def next(self, price: int) -> int:
        self.stockSpanner.append(price)
        self.size += 1
        for i in range(self.size - 1, -1, -1):
            if self.stockSpanner[i] > price:
                return self.size - i - 1
        return self.size
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)