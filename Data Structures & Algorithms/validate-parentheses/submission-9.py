class Solution:
    def isValid(self, s: str) -> bool:
        opens = []

        pairs = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        for char in s:
            if char in pairs:
                opens.append(char)
            else:
                if not opens or pairs[opens.pop()] != char:
                    return False
        
        return not opens


