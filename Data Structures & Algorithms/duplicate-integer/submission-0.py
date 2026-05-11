class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)
        freq={}
        for x in nums:
            freq[x]=freq.get(x,0)+1
        for value in freq.values():
            if(value>1):
                return True
            
        return False



        