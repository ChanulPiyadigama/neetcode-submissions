from math import sqrt
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not points:
            return []

        maxHeap = []

        for x,y in points:
            dist= sqrt(x**2+y**2)

            if len(maxHeap) < k:
                heapq.heappush(maxHeap, (-dist, [x, y]))
            elif dist < -(maxHeap[0][0]):
                heapq.heappop(maxHeap) 
                heapq.heappush(maxHeap, (-dist, [x, y]))
        
        return [pair[1] for pair in maxHeap]
            




