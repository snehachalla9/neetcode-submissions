class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq={}
        for x in s:
            freq[x]=freq.get(x,0)+1
        for x in t:
            freq[x]=freq.get(x,0)-1
        return all(v==0 for v in freq.values())
        

        