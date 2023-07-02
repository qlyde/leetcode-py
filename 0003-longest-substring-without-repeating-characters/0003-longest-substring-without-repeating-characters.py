class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        l = 0
        ret = 0

        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            ret = max(ret, r - l + 1)
        
        return ret
