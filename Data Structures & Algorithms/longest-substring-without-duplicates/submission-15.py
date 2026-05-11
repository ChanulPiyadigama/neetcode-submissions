class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        seen = set()
        maxLength = 0
        start = 0

        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[start])
                start += 1
            seen.add(s[i])
            maxLength = max(maxLength, len(seen))

        return maxLength
