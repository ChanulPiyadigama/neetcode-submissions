class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        counts = defaultdict(int)
        freq_buckets = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            counts[num] += 1
        
        for num, freq in counts.items():
            freq_buckets[freq].append(num)
        
        for i in range(len(freq_buckets) - 1, 0, -1):
            for num in freq_buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res

        

