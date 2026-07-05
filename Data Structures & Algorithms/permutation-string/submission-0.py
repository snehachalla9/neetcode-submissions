class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # freq={}
        # for x in s1:
        #     freq[x]=freq.get(x,0)+1
        # for x in s2:
        #     freq[x]=freq.get(x,0)-1
        # return all(v==0 for v in freq.values())
        n=len(s2)
        n1=len(s1)
        left=0
        freq={}
        for x in s1:
            freq[x]=freq.get(x,0)+1
        freq2={}
        for right in range(n):
            freq2[s2[right]] = freq2.get(s2[right], 0) + 1
            window_s=right-left+1
            if window_s>n1:
                freq2[s2[left]] -= 1
                if freq2[s2[left]] == 0:
                    del freq2[s2[left]]
                left += 1
            if right-left+1==n1:
                if freq==freq2:
                    return True
        return False


