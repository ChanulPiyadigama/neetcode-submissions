class Solution:
    def generateParenthesis(self, n: int) -> List[str]:


        res = []


        strings = [('(',1,0)]
        while strings:
            newStrings = []
            for s in strings:
                string, opened, closed = s
                if opened > closed:
                    newStrings.append((string + ')', opened, closed+1))
                if opened < n:
                    newStrings.append((string + '(', opened+1, closed))
                if closed == opened == n:
                    res.append(string)
            strings = newStrings
        return res

                

