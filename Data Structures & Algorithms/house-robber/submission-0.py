class Solution:
    def rob(self, nums: List[int]) -> int:
        dp={}
        def robb(i):
            if i>=len(nums):
                return 0
            if i in dp:
                return dp[i]
            rob_c=nums[i]+robb(i+2)
            skip_c=robb(i+1)
            dp[i]=max(rob_c,skip_c)
            return dp[i]
        return robb(0)
        