class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R, C = len(matrix), len(matrix[0])
        top = 0
        bot = R - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        
        if not top <= bot:
            return False

        l, r = 0, C - 1
        row = (top + bot) // 2
        while l <= r:
            t = (l + r) // 2
            if target > matrix[row][t]:
                l = t + 1
            elif target < matrix[row][t]:
                r = t - 1
            elif target == matrix[row][t]:
                return True
        return False 