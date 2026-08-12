class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        Subs = set()
        longest = 0

        for r in range(len(s)):
            while s[r] in Subs:
                Subs.remove(s[l])
                l+=1
            
            Subs.add(s[r])

            longest = max(longest, len(Subs))

        return longest
