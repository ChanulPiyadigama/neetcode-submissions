class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True


        stack = []

        pairs = {
            '(': ')',
            '{': '}',
            '[':']'
        }
        
        for i in s:
            if i in pairs.keys():
                stack.append(i)
            else:
                if not stack:
                    return False
                opener = stack.pop()
                if i != pairs[opener]:
                    return False
        
        if len(stack)!=0 :
            return False
        return True 


