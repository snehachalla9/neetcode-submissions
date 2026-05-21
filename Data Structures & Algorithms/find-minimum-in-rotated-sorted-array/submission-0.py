class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        in linear search we get time complexity of O(n)
        minimum=nums[0]
        for num in nums:
            if num<minimum:
                minimum=num
        return minimum
        """
        #But we want O(log n) so we should use binary search method
        left=0
        n=len(nums)
        right=n-1
        while left<right:
            mid=(left+right)//2
            if nums[mid]>nums[right]:
                left=mid+1
            else:
                right=mid
        return nums[left]

        