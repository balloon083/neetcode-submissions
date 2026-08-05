class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        res = []

        while not res:
            if (numbers[left] + numbers[right] > target):
                right -= 1
            elif (numbers[left] + numbers[right] < target):
                left += 1
            else:
                res = [left + 1, right + 1]
        return res