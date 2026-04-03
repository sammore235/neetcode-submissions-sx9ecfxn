class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits=[]
        for i in range(0,len(prices)):
            for j in range(i+1,len(prices)):
                if prices[i]<prices[j]:
                    k = prices[j]-prices[i]
                    profits.append(k)
                else:
                    continue

        profits_asc = sorted(profits)
        if profits_asc==[]:
            return 0
        else:
            return profits_asc[-1]