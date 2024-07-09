class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)-1
        while l < r:
            mid = l + (r-l)//2
            if matrix[mid][-1] >= target:
                r = mid
            else:
                l = mid + 1
        row = l
        l = 0
        r = len(matrix[0])-1
        while l < r:
            mid = l + (r-l)//2
            if matrix[row][mid] >= target:
                r = mid
            else:
                l = mid + 1
        return True if matrix[row][l] == target else False
        
