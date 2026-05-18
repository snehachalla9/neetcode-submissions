class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        left=0
        right=1
        max_p=0
        while right<n:
            if prices[right]>prices[left]:
                p=prices[right]-prices[left]
                max_p=max(p,max_p)
            else:
                left=right
            right+=1
        return max_p
        


        