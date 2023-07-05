class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ret = []
        q = collections.deque()
        l = 0
        for r in range(len(nums)):
            while q and nums[r] > nums[q[-1]]:
                q.pop()

            q.append(r)

            if l > q[0]:
                q.popleft()

            # complete window
            if r + 1 >= k:
                l += 1
                ret.append(nums[q[0]])
        return ret