class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        l = 0
        ret = 0

        for r in range(len(s)):
            count[ord(s[r]) - ord("A")] += 1

            while r - l + 1 - max(count) > k:
                count[ord(s[l]) - ord("A")] -= 1
                l += 1
            
            ret = max(ret, r - l + 1)

        return ret
