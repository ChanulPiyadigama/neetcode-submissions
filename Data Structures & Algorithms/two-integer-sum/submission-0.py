class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            requiredNum = target - nums[i]
            if (requiredNum) in dict:
                requiredIdx = dict[requiredNum]
                return [requiredIdx, i]
            dict[nums[i]] = i
