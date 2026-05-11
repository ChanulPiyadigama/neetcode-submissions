class Solution:
    def isValid(self, s: str) -> bool:
        opens = []

        pairs = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        for i in range(len(s)):
            if s[i] in pairs.values():
                if not opens:
                    return False
                else:
                    pair = opens.pop()
                    if pairs[pair] != s[i]:
                        return False
            else:
                opens.append(s[i])
        
        if opens:
            return False
        return True


