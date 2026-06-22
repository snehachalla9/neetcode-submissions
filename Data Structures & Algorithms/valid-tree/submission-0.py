from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph={i:[] for i in range(n)}
        for u,v in edges:
            graph[v].append(u)
            graph[u].append(v)
        q=deque([(0,-1)])
        visited=set([0])
        visited.add(0)
        while q:
            node,parent=q.popleft()
            for neigh in graph[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    q.append((neigh,node))
                elif neigh!=parent:
                        return False
        return len(visited)==n