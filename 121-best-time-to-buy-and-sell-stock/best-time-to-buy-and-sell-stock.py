class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        cheap = prices[0]
        best_case_profit = 0

        for i in range(1, len(prices)):
            if prices[i] < cheap:
                cheap = prices[i]

            profit = prices[i] - cheap

            if profit > best_case_profit:
                best_case_profit = profit
            
        return best_case_profit


        