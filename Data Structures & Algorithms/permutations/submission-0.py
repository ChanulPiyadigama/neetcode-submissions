class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res= []

        p = []
        used = [False] * len(nums)

        def dfs():
            if len(p) == len(nums):
                res.append(list(p))
                return
            
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    p.append(nums[i])
                    dfs()
                    p.pop()
                    used[i] = False
        dfs()
        return res
            