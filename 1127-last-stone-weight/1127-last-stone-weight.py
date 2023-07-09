class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            h1 = heapq.heappop(stones)
            h2 = heapq.heappop(stones)
            if h1 != h2:
                heapq.heappush(stones, h1 - h2)
        return -stones[0] if len(stones) > 0 else 0
