class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans=""
        max_l=0
        dp={}
        n=len(s)
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
        for i in range(0,n):
            for j in range(i,n):
                if solve(i,j)==True:
                    leng=j-i+1
                    if leng>max_l:
                        max_l=leng
                        ans=s[i:j+1]
        return ans
             