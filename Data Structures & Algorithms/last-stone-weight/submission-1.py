import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[-stone for stone in stones]
        heapq.heapify(heap)
        while len(heap)>1:
            x=-heapq.heappop(heap)
            y=-heapq.heappop(heap)
            if x==y:
                pass
            else:
                heapq.heappush(heap,-(x-y))
        if not heap:
            return 0
        else:
            return -heap[0]

