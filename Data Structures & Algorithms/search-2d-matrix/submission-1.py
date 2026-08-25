class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find the row first
        first, last = 0, len(matrix) - 1
        can_find = False
        while first <= last:
            row = (first + last) // 2
            if matrix[row][0] <= target and matrix[row][len(matrix[0])-1] >= target:
                can_find = True
                break
            if matrix[row][0] > target:
                last = row - 1
            else:
                first = row + 1
        if can_find:
            l, r = 0, len(matrix[0]) - 1
            while l <= r:
                mid = (l + r) // 2
                if matrix[row][mid] == target:
                    return True
                elif matrix[row][mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
        return False