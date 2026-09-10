class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest_price=prices[0]
        max_profit=0
        for i in prices:
            cheapest_price=min(cheapest_price,i)
            profit_curr=i-cheapest_price
            max_profit=max(max_profit,profit_curr)
        return max_profit
        