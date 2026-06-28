class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left =1
        right = max(piles)

        def canEatAll(k):
            totalHours = 0
            for p in piles:
                totalHours += (p + k - 1) // k
                if totalHours > h:
                    return False
            return True

        while left < right:
            mid = left + (right -left) // 2

            if canEatAll(mid):
                right = mid
            else:
                left = mid + 1
        
        return left