class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp={}
        n=len(coins)
        def solve(i,remain):
            if remain==0:
                return 0
            if remain<0 or i==n:
                return float('inf')
            if (i,remain) in dp:
                return dp[(i,remain)]
            take=1+solve(i,remain-coins[i])#we have already used one coin
            not_take=solve(i+1,remain)
            dp[(i,remain)]=min(take,not_take)
            return dp[(i,remain)]
        ans=solve(0,amount)
        return -1 if ans==float('inf') else ans