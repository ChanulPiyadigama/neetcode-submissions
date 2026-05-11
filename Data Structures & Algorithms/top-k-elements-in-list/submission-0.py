class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        counts = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] +=1

        print(counts)
        for num, count in dict.items():
            counts[count].append(num)
        
        print(counts)
        values = []
        for numList in reversed(counts):
            if len(numList) != 0 :
                for num in numList:
                    values.append(num)
                    k -= 1
            if k == 0:
                break 
        
        return values 


        