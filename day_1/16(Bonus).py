import math
import os

def diagonalDifference(arr):
    primary_sum = 0
    secondary_sum = 0
    n = len(arr)
    
    for i in range(n):
        primary_sum += arr[i][i]          
        secondary_sum += arr[i][n - 1 - i] 
        
    return abs(primary_sum - secondary_sum)


sample_matrix = [
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12]
]
    
result = diagonalDifference(sample_matrix)
print(f"Absolute Diagonal Difference: {result}")