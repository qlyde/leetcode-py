class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        def backtrack(i, curr=[], total=0):
            if total == target:
                ret.append(list(curr))
                return
            
            if i >= len(candidates) or total > target:
                return

            curr.append(candidates[i])
            backtrack(i, curr, total + candidates[i])
            curr.pop()
            backtrack(i + 1, curr, total)
        backtrack(0)
        return ret
