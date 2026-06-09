class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def backtracking(index,target,path):
            if(index==len(nums)):
                return
            if target==0:
                res.append(path[:])
                return
            if nums[index]<=target:
                path.append(nums[index])
                backtracking(index,target-nums[index],path)
                path.pop()
            backtracking(index+1,target,path)
        backtracking(0,target,[])
        return res
        

        