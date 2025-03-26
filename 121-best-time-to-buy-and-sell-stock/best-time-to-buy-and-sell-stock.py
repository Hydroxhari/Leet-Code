class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0
        
        # Iterate through the price list
        for price in prices:
            # Update minimum price if a lower price is found
            min_price = min(min_price, price)
            
            # Calculate profit if we sell at the current price
            profit = price - min_price
            
            # Update max profit if we get a higher profit
            max_profit = max(max_profit, profit)
        
        return max_profit