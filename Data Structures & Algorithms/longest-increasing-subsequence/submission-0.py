class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp={}
        def solve(i,prev):
            if i==n:
                return 0
            if (i,prev) in dp:
                return dp[(i,prev)]
            take=0
            if prev==-1 or nums[i]>nums[prev]:
                take=1+solve(i+1,i)
            skip=solve(i+1,prev)
            dp[(i,prev)]=max(take,skip)
            return dp[(i,prev)]
        return solve(0,-1)