class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_en=nums[0]
        min_en=nums[0]
        ans=nums[0]
        n=len(nums)
        for i in range(1,n):
            c1=nums[i]
            c2=c1*max_en
            c3=c1*min_en
            new_m=max(c1,c2,c3)
            new_min=min(c1,c2,c3)
            max_en=new_m
            min_en=new_min
            ans=max(ans,new_m)
        return ans
        
        
        