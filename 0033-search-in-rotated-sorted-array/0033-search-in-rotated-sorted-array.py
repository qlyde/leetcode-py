class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m

            if nums[m] >= nums[l]:
                # m in left side
                if nums[m] < target or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1

            else:
                # m in right side
                if nums[m] > target or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
                
        return -1
