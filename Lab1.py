import unittest

def zigzag(matrix):
    if not matrix or not matrix[0]:
        return []
        
    m = len(matrix)
    n = len(matrix[0])
    result = []
    
   
    for s in range(m + n - 1):
        if s % 2 == 0:
            row = min(s,
                       m - 1)
            col = s - row
            while row >= 0 and col < n:
                result.append(matrix[row][col])
                row -= 1
                col += 1
        else:
            col = min(s, n - 1)
            row = s - col
            while col >= 0 and row < m:
                result.append(matrix[row][col])
                row += 1
                col -= 1
                
    return result

def my_min(lst):
    if not lst:
        raise ValueError("my_min() arg is an empty sequence")
    smallest = lst[0]
    for item in lst[1:]:
        if item < smallest:
            smallest = item
    return smallest
