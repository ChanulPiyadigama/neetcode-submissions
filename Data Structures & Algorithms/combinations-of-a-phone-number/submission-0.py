class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitsMap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res = []
        l = []
        if not digits:
            return res
        def dfs(i):
            if i == len(digits):
                res.append(''.join(l))
                return 
            
            for j in digitsMap[digits[i]]:
                l.append(j)
                dfs(i+1)
                l.pop()
        dfs(0)
        return res
        

