class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n=len(s)
        freq={}
        have=0
        for ch in t:
            freq[ch]=freq.get(ch,0)+1
        need=len(freq)
        window={}
        res=[-1,-1]
        min_s=float('inf')
        left=0
        for right in range(n):
            window[s[right]]=window.get(s[right],0)+1
            if s[right] in freq and window[s[right]]==freq[s[right]]:
                have+=1
            while have==need:
                if (right-left+1<min_s):
                    min_s=right-left+1
                    res=[left,right]
                window[s[left]]-=1
                if s[left] in freq and window[s[left]] <freq[s[left]]:
                    have-=1
                left+=1
        left,right=res
        return s[left:right+1] if min_s != float('inf') else ""

        
        


        