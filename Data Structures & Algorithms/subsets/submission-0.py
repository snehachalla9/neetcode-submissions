class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # result=[]
        # def back(start,path):
        #     result.append(path.copy())
        #     for i in range(start,len(nums)):
        #         path.append(nums[i])
        #         back(i+1,path)
        #         path.pop()
        # back(0,[])
        # return result
        result=[]
        def back(i,path):
            if i==len(nums):
                result.append(path.copy())
                return
            path.append(nums[i])
            back(i+1,path)
            path.pop()
            back(i+1,path)
        back(0,[])
        return result
        