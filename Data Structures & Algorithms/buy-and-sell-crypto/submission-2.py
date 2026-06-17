class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mins = [prices[0]]
        for i in range(len(prices)):
            if i != 0:
                mins.append(min(prices[0:i]))
        
        best = 0
        for i in range(len(prices)):
            if prices[i] - mins[i] > best:
                best = prices[i]-mins[i]
            
        return best