class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l <= r:
            k = l + (r - l) // 2
            hrs = sum([math.ceil(b / k) for b in piles])
            if hrs > h:
                l = k + 1
            else:
                r = k - 1
        return l

# k = [1, max(piles)]
