class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainders = {}

        for i in range(len(nums)):
            if nums[i] in remainders:
                return [remainders[nums[i]], i]
            r = target - nums[i]
            remainders[r] = i
