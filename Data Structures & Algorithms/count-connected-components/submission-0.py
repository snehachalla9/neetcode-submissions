from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph={ i:[] for i in range(n)}
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited=set()
        c=0
        for node in range(n):
            if node not in visited:
                c+=1
                q=deque([node])
                visited.add(node)
                while q:
                    curr=q.popleft()
                    for neigh in graph[curr]:
                        if neigh not in visited:
                            visited.add(neigh)
                            q.append(neigh)
        return c
            
                
                

        