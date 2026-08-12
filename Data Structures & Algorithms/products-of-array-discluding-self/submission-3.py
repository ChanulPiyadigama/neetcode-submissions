class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        leftCount = 1

        for i in range(n):
            res[i] *= leftCount
            leftCount *= nums[i]
        
        rightCount = 1
        for i in range(n - 1, -1, -1):
            res[i] *= rightCount
            rightCount *= nums[i]
        
        return res


        



        