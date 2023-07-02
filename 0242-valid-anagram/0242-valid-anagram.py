class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        charsS, charsT = {}, {}
        for i in range(len(s)):
            charsS[s[i]] = charsS.get(s[i], 0) + 1
            charsT[t[i]] = charsT.get(t[i], 0) + 1
        return charsS == charsT
