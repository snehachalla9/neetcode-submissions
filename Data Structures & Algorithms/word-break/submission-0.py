class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp={}
        n=len(s)
        wordset=set(wordDict)
        def solve(i):
            if i==len(s):
                return True
            if i in dp:
                return dp[i]
            for j in range(i+1,n+1):
                if s[i:j] in wordset:
                    if solve(j):
                        dp[i]=True
                        return dp[i]
            dp[i]=False
            return dp[i]
        return solve(0)        