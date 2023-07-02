class Solution:
    def trap(self, height: List[int]) -> int:
        # min(maxL, maxR) - h[i]
        l, r = 0, len(height) - 1
        maxL, maxR = 0, 0
        maxLs, maxRs = [0] * len(height), [0] * len(height)

        while r >= 0:
            maxLs[l] = maxL
            maxRs[r] = maxR

            maxL = max(maxL, height[l])
            maxR = max(maxR, height[r])

            l += 1
            r -= 1

        ret = 0
        for i in range(len(height)):
            ret += max(0, min(maxLs[i], maxRs[i]) - height[i])

        return ret
