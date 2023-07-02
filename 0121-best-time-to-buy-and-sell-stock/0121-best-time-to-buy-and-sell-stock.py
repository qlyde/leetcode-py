class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret = 0
        lowest = prices[0]

        for price in prices:
            if price < lowest:
                lowest = price
            
            ret = max(ret, price - lowest)
        return ret
