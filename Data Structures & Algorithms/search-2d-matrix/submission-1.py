class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        t, b = 0, len(matrix) - 1
        
        # First binary search: find the correct row
        while t <= b:
            m = (t + b) // 2
            
            # Check if target is in this row's range
            if target < matrix[m][0]:
                b = m - 1  # Target is above this row
            elif target > matrix[m][-1]:
                t = m + 1  # Target is below this row
            else:
                # Target is in this row, now search within the row
                l, r = 0, len(matrix[m]) - 1
                
                while l <= r:
                    n = (l + r) // 2
                    if matrix[m][n] == target:
                        return True
                    elif matrix[m][n] < target:
                        l = n + 1
                    else:
                        r = n - 1
                
                return False  # Target not found in the correct row
        
        return False  # Target not found in any row