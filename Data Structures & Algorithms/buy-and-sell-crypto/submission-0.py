class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            j = i+1
            while (j<=len(prices)-1):
                if prices[j] > prices[i]:
                    profit = max(profit,(prices[j] - prices[i]))
                print(i,j)
                j += 1
        return profit
            
                
                
            
            
        