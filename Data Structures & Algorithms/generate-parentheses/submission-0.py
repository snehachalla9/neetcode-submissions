class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        def parenth(curr,open,close):
            if len(curr)==2*n:
                result.append(curr)
                return
            if open<n:
                parenth(curr+"(",open+1,close)
            if close<open:
                parenth(curr+")",open,close+1)
        parenth("",0,0)
        return result
        