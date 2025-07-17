# Last updated: 7/17/2025, 7:56:03 PM
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col_len = len(matrix[0]) 
        left = 0
        right = col_len * len(matrix) - 1

        while left <= right:
            mid = (left + right) // 2
            r = mid // col_len
            c = mid % col_len

            if matrix[r][c] >= target:
                right = mid - 1
            else:
                left = mid + 1
        
        r = left // col_len
        c = left % col_len
        if r < len(matrix) and c < col_len and matrix[r][c] == target:
            return True
        return False

# idx = column_length * row + column