class Solution:
    def maxProfit(self, prices):
        minprice = prices[0]
        maxprofit = 0
        for price in prices:
            minprice = min(minprice, price)
            if minprice > maxprofit:
                maxprofit = minprice



prices=[7,1,5,3,6,4]
print(Solution().maxProfit(prices))