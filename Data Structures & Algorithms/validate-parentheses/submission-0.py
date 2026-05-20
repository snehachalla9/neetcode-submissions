class Solution:
    def isValid(self, s: str) -> bool:
        n=len(s)
        st=[]
        dict={')':'(',']':'[','}':'{'}
        for ch in s:
            if ch=='(' or ch=='[' or ch=='{':
                st.append(ch)
            else:
                if not st:
                    return False
                if st[-1]!=dict[ch]:
                    return False
                st.pop()
        return len(st)==0


        