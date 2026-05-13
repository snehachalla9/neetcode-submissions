class Solution:

    def encode(self, strs: List[str]) -> str:
        result=""
        for word in strs:
            result+=str(len(word))+'#'+word
        return result

    def decode(self, s: str) -> List[str]:
        re=[]
        n=len(s)
        i=0
        while i<n:
            j=i
            while s[j]!='#':
                j+=1
            length=int(s[i:j])
            word=s[j+1:j+1+length]
            re.append(word)
            i=j+1+length
        return re



