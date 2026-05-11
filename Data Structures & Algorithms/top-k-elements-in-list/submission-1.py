class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        buckets = [[] for _ in nums]
        res = []

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        for key, value in counts.items():
            buckets[value - 1].append(key)

        done = False
        for bucket in reversed(buckets):
            for key in bucket:
                res.append(key)
                k -= 1
                if k == 0:
                    done = True
                    break
            if done:
                break
        return res




        