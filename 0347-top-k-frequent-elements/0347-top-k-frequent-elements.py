class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        freqs = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        for num, count in counts.items():
            freqs[count].append(num)

        ret = []
        for freq in freqs[::-1]:
            for num in freq:
                ret.append(num)
                if len(ret) == k:
                    return ret
        return []
        

