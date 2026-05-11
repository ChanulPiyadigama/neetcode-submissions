class Solution:
    def generateParenthesis(self, n: int) -> List[str]:


        res = self.generateParenthesisRec(('(', 1,0), n, [])
        print(res)
        return res

    def generateParenthesisRec(self, s, limit, res):
        string, opened, closed = s
        if opened > closed:
            res1 = self.generateParenthesisRec((string + ')',opened, closed+1),limit, res)
        if opened < limit:
            res2 = self.generateParenthesisRec((string+'(', opened+1, closed),limit, res)
        if opened == closed == limit:
            res.append(string)
        return res

