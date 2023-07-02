class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-4, -1, -1, 0, 1, 2]
        nums.sort()
        ret = []

        for idx, num in enumerate(nums):
            if num > 0:
                break

            # Skip duplicate negative numbers
            if idx > 0 and num == nums[idx - 1]:
                continue

            l, r = idx + 1, len(nums) - 1
            while l < r:
                s = num + nums[l] + nums[r]
                if s == 0:
                    ret.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif s < 0:
                    l += 1
                else:
                    r -= 1

        return ret
