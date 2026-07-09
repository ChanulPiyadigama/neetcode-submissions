class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        

        def robHouses(houses):
            prev1, prev2 = 0, 0
            for m in houses:
                current = max(m + prev2, prev1)
                prev2 = prev1
                prev1 = current
            return prev1
        
        return max(robHouses(nums[:-1]), robHouses(nums[1:]))

