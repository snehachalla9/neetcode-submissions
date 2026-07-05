class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        numbers.sort()
        left=0
        right=n-1
        result=[]
        while left<right:
            s=numbers[left]+numbers[right]
            if s==target:
                result.extend([left+1,right+1])
                left+=1
                right-=1
            elif s<target:
                left+=1
            else:
                right-=1
        return result