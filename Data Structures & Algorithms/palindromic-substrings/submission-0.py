class Solution:
    def countSubstrings(self, s: str) -> int:
        dp={}
        n=len(s)
        c=0
        def solve(i,j):
            if i>=j:
                return True
            if (i,j) in dp:
                return dp[(i,j)]
            if s[i]!=s[j]:
                dp[(i,j)]=False
                return False
            dp[(i,j)]=solve(i+1,j-1)
            return dp[(i,j)]
        for i in range(n):
            for j in range(i,n):
                if solve(i,j):
                    c+=1
        return c
