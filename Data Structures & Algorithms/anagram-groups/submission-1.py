class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            strMakeup = [0] * 26
            for c in s:
                strMakeup[ord(c) - ord('a')] += 1
            
            strMakeupTuple = tuple(strMakeup)

            anagrams[strMakeupTuple].append(s)

        return [a for a in anagrams.values()]
