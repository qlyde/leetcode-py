class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ds = [(sqrt(y * y + x * x), x, y) for [x, y] in points]
        heapq.heapify(ds)
        ret = []
        for _ in range(k):
            d, x, y = heapq.heappop(ds)
            ret.append([x, y])
        return ret
