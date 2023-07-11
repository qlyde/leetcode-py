class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        curr = []
        def backtrack(i):
            if i >= len(nums):
                ret.append(list(curr))
                return
            curr.append(nums[i])
            backtrack(i + 1)
            curr.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1)

        backtrack(0)
        return ret
