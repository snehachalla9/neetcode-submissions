import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        result=[]
        for point in points:
            x=point[0]
            y=point[1]
            dist=(x*x+y*y)
            heapq.heappush(heap,(-dist,[x,y]))
            if len(heap)>k:
                heapq.heappop(heap)
        return [point for _,point in heap]