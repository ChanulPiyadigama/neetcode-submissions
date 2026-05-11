class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def dfs(opens, closes, curr):
            if opens == 0 and closes == 0:
                res.append(''.join(c for c in curr))
                return
            if opens > 0:
                curr.append("(")
                dfs(opens-1, closes, curr)
                curr.pop()
            if closes > 0 and opens < closes:
                curr.append(")")
                dfs(opens, closes-1, curr)
                curr.pop()
            return 
        dfs(n,n,[])
        return res
             

