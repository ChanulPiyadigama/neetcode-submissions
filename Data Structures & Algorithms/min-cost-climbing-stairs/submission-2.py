class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Iterate backwards starting from the 3rd to last element
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
            
        # The top of the stairs can be reached from either index 0 or index 1
        return min(cost[0], cost[1])