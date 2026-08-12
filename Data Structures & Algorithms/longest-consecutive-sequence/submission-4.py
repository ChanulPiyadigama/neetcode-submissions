class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            behind = 0
            curr = n
            while (curr-1) in numSet:
                numSet.remove(curr-1)
                curr -= 1
                behind += 1
                

            ahead = 0
            curr = n
            while (curr + 1) in numSet:
                numSet.remove(curr+1)
                curr += 1
                ahead += 1
            
            longest = max(longest, (behind + ahead + 1))

        return longest 
            




