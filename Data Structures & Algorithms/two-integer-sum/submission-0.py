class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        placeholdermap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in placeholdermap:
                return [placeholdermap[diff], i]
            placeholdermap[n] = i