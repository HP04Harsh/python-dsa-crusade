# 122. Best Time to Buy and Sell Stock II
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        n = len(prices)

        for i in range(n-1):
            if prices[i+1]>prices[i]:
                profit += (prices[i+1]-prices[i])
        return profit        


        