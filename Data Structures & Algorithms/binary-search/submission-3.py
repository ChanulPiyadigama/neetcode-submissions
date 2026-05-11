class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(start, end, nums, target):
            if start > end:
                return -1
            mid = (start + end) // 2
            
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
               return binarySearch(start, mid - 1, nums, target)
            else:
                return binarySearch(mid+1, end, nums, target)
             
        return binarySearch(0, len(nums)-1, nums, target)

