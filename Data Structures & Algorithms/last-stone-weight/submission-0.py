import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-i for i in stones]
        heapq.heapify(maxHeap)
        
        while len(maxHeap) > 1:
            print(maxHeap)
            val1, val2 = -heapq.heappop(maxHeap), -heapq.heappop(maxHeap)
            print(val1, val2)
            if val1 > val2:
                remainingStone = val1 - val2
            elif val2 > val1:
                remainingStone = val2-val1
            else:
                remainingStone = 0
            
            if remainingStone != 0:
                heapq.heappush(maxHeap, -remainingStone)
        
        if len(maxHeap) == 1:
            return -heapq.heappop(maxHeap)
        else:
            return 0
