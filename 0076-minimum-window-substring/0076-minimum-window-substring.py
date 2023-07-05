class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        tCount, wCount = {}, {}
        for ch in t:
            tCount[ch] = tCount.get(ch, 0) + 1
        
        ret, retLen = (-1, -1), float("infinity")
        have, need = 0, len(t)
        l = 0
        for r in range(len(s)):
            if s[r] in tCount:
                wCount[s[r]] = wCount.get(s[r], 0) + 1

                # check if new window character is necessary
                if wCount[s[r]] <= tCount[s[r]]:
                    have += 1

            while have >= need:
                if r - l + 1 < retLen:
                    ret, retLen = (l, r), r - l + 1

                # advance l until have < need
                if s[l] in wCount:
                    wCount[s[l]] -= 1
                    # check if popped l is necessary
                    if wCount[s[l]] < tCount[s[l]]:
                        have -= 1
                l += 1

        return s[ret[0] : ret[1] + 1] # s[-1:0] = ''
