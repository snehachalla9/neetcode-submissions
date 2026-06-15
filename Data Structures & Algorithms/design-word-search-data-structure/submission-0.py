class WordDictionary:

    def __init__(self):
        self.dict={}
        self.isend=False
        

    def addWord(self, word: str) -> None:
        node=self
        for ch  in word:
            if ch not in node.dict:
                node.dict[ch]=WordDictionary()
            node=node.dict[ch]
        node.isend=True
        

    def search(self, word: str) -> bool:
        def dfs(i,node):
            if i==len(word):
                return node.isend
            ch=word[i]
            if ch=='.':
                for val in node.dict.values():
                    if dfs(i+1,val):
                        return True
                return False
            if ch not in node.dict:
                return False
            return dfs(i+1,node.dict[ch])
        return dfs(0,self)
        
