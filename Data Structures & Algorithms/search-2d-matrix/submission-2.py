class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        t, b = 0, len(matrix) - 1
        
        while t <= b:
            m = (t + b) // 2
            
            if target < matrix[m][0]:
                b = m - 1  
            elif target > matrix[m][-1]:
                t = m + 1  
            else:
                
                l, r = 0, len(matrix[m]) - 1
                
                while l <= r:
                    n = (l + r) // 2
                    if matrix[m][n] == target:
                        return True
                    elif matrix[m][n] < target:
                        l = n + 1
                    else:
                        r = n - 1
                
                return False  
                
        return False 