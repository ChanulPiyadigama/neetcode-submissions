class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1Characters = {}
        s2Characters = {}
        for i in range(len(s1)):
            s1Characters[s1[i]] = s1Characters.get(s1[i], 0) + 1
            s2Characters[s2[i]] = s2Characters.get(s2[i], 0) + 1

        if s1Characters == s2Characters: return True

        l=1
        for r in range(len(s1), len(s2)):
            s2Characters[s2[r]] = s2Characters.get(s2[r], 0) + 1
            s2Characters[s2[l-1]] -=1
            if s2Characters[s2[l-1]] == 0:
                del s2Characters[s2[l-1]]
            l+=1
            if s1Characters == s2Characters: return True
        return False 




            
            
