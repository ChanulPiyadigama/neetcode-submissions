import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-i for i in stones]
        heapq.heapify(maxHeap)
        
        while len(maxHeap) > 1:
            val1, val2 = -heapq.heappop(maxHeap), -heapq.heappop(maxHeap)

            if val1 != val2:
                heapq.heappush(maxHeap, -(val1 - val2))
            
        return -maxHeap[0] if maxHeap else 0

