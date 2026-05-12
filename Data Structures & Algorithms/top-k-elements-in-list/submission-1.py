class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        result=[]
        for x in nums:
            freq[x]=freq.get(x,0)+1
        sorted_freq=sorted(freq.items(),key=lambda x:x[1],reverse=True)
        for key,value in sorted_freq[:k]:
            result.append(key)
        return result
        