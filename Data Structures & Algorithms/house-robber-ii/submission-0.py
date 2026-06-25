class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def solve(arr):
            dp={}
            def robb(i):
                if i>=len(arr):
                    return 0
                if i in dp:
                    return dp[i]
                rob_c=arr[i]+robb(i+2)
                skip=robb(i+1)
                dp[i]=max(rob_c,skip)
                return dp[i]
            return robb(0)
        ans1=solve(nums[:-1])
        ans2=solve(nums[1:])
        return max(ans1,ans2)
        
        