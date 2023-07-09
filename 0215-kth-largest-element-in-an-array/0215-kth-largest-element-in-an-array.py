# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         nums = [-num for num in nums]
#         heapq.heapify(nums)
#         for _ in range(k - 1):
#             heapq.heappop(nums)
#         return -heapq.heappop(nums)

# QuickSelect
class Solution:
    def partition(self, nums, left, right):
        pivot, fill = nums[right], left

        for i in range(left, right):
            if nums[i] <= pivot:
                nums[fill], nums[i] = nums[i], nums[fill]
                fill += 1
        
        nums[fill], nums[right] = nums[right], nums[fill]
        return fill

    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        left, right = 0, len(nums) - 1
    
        while left < right:
            pivot = self.partition(nums, left, right)

            if pivot < k:
                left = pivot + 1
            elif pivot > k:
                right = pivot - 1
            else:
                break
        
        return nums[k]