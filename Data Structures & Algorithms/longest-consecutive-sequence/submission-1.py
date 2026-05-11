class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()

        for num in nums:
            numSet.add(num)
        
        maxLen = 0

        for num in nums:
            if (num - 1) not in numSet:
                sequenceLen = 1
                while True:
                    if num+1 in numSet:
                        sequenceLen+=1
                        num +=1
                    else:
                        break 
                maxLen = max(sequenceLen, maxLen)
        return maxLen 


