class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        cols=len(matrix[0])
        total=rows*cols
        left=0
        right=total-1
        while right>=left:
            mid=(left+right)//2
            row = mid // cols
            col = mid % cols
            if target==matrix[row][col]:
                return True
            elif target> matrix[row][col]:
                left =mid+1
            else:
                right=mid-1
        return False