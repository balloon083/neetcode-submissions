class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while(low <= high):
            index = low + ((high - low) // 2)
            if(nums[index] < target):
                low = index + 1
            elif(nums[index] > target):
                high = index - 1
            else: return index
        return -1
            
