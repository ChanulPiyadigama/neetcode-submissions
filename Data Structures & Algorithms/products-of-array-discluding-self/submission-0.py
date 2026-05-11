class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)

        totalProduct = 1
        zeros = 0
        for num in nums:
            if num == 0:
                zeros+=1
                continue
            totalProduct *= num
        
        if zeros < 2 :
            if zeros == 1:
                for idx, num in enumerate(nums):
                    if num == 0:
                        output[idx] = totalProduct
                    else:
                        output[idx] = 0
            else:
                for idx, num in enumerate(nums):
                    output[idx] = totalProduct//num
        return output
        