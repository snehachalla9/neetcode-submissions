import heapq
class MedianFinder:
 
    def __init__(self):
        self.left=[]
        self.right=[]
    def addNum(self, num: int) -> None:
        if not self.left or num<=-self.left[0]:
            heapq.heappush(self.left,-num)
        else:
            heapq.heappush(self.right,num)
        if len(self.left)>len(self.right)+1:
            heapq.heappush(self.right,-heapq.heappop(self.left))
        elif len(self.right)>len(self.left)+1:
            heapq.heappush(self.left,-heapq.heappop(self.right))
        if self.left and self.right and -self.left[0]>self.right[0]:
            leftmax=-heapq.heappop(self.left)
            rightmin=heapq.heappop(self.right)
            heapq.heappush(self.left,-rightmin)
            heapq.heappush(self.right,leftmax)

    def findMedian(self) -> float:
        if len(self.left)>len(self.right):
            return -self.left[0]
        elif len(self.right)>len(self.left):
            return self.right[0]
        return (-self.left[0]+self.right[0])/2

        
        