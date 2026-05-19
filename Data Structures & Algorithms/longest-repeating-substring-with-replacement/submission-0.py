class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        n=len(s)
        freq={}
        max_freq=0
        ans=0
        for right in range(n):
            freq[s[right]]=freq.get(s[right],0)+1
            max_freq=max(max_freq,freq[s[right]])
            window_size=right-left+1
            if window_size-max_freq>k:
                freq[s[left]]-=1
                left+=1
            ans=max(max_freq,right-left+1)
        return ans
            



        