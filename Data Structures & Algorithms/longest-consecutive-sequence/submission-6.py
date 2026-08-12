class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            # Check if 'n' is the START of a consecutive sequence
            if (n - 1) not in numSet:
                length = 1
                # Track forward to find the end of the sequence
                while (n + length) in numSet:
                    length += 1
                
                longest = max(longest, length)

        return longest
