class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(0, len(nums)-1, target, nums)
    
    def binarySearch(self, left, right, target, nums):
        if left > right:
            return -1
        
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            return self.binarySearch(left, mid-1, target, nums)
        else:
            return self.binarySearch(mid+1, right, target, nums)