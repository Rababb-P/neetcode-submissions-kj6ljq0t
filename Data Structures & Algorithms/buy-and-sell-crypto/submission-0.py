class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        buy = prices[0]

        for sell in prices:
            if maxp < sell - buy:
                maxp = sell - buy
            if sell < buy:
                buy = sell
        return maxp