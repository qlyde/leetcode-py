class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in h:
                return [h[complement], idx]
            h[num] = idx
        return []





