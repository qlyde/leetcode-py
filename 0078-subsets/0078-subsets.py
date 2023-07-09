class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        curr = []
        def backtrack(i):
            if i >= len(nums):
                ret.append(list(curr))
                return
            curr.append(nums[i])
            backtrack(i + 1)
            curr.pop()
            backtrack(i + 1)
        backtrack(0)
        return ret
