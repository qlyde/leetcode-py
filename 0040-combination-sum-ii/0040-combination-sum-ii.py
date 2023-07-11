class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(nums, target, i, curr, currSum, ret):
            if currSum == target:
                ret.append(list(curr))
                return
            if currSum > target or i >= len(nums):
                return
            curr.append(nums[i])
            dfs(nums, target, i + 1, curr, currSum + nums[i], ret)
            curr.pop()
            while i + 1 < len(candidates) and nums[i] == nums[i + 1]:
                i += 1
            dfs(nums, target, i + 1, curr, currSum, ret)
        ret = []
        candidates.sort()
        dfs(candidates, target, 0, [], 0, ret)
        return ret
            
