class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset= set(nums)
        longest = 0

        for num in nums:
            if (num-1) not in nset:
                currLen = 1
                while num+1 in nset:
                    currLen+=1
                    num+=1
                if currLen > longest:
                    longest =currLen
        return longest

                    