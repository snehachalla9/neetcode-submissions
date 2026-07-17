class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result=[]
        path=[]
        def polin(left,right):
            while left<right:
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True
        def back(start):
            if start==len(s):
                result.append(path.copy())
                return
            for end in range(start,len(s)):
                if polin(start,end):
                    path.append(s[start:end+1])
                    back(end+1)
                    path.pop()
        back(0)
        return result
