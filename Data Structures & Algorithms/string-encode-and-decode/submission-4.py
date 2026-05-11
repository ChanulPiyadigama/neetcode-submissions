class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedMess = ""

        for s in strs:
            encodedMess += str(len(s)) + "#" + s
        return encodedMess 

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            
            j = i
            while s[j] != "#":
                j+=1                
            
            length = int(s[i : j])

            i = j + 1

            w = s[i : i + length]
            res.append(w)

            i = i + length
        return res