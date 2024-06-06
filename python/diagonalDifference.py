#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    cols = len(arr)
    rows = len(arr[0])
    length = cols
    if cols < rows:
        length = rows
    row_left_start = 0
    col_start = 0
    row_r_start = length - 1
    sum_left = 0
    sum_right = 0

    while length > 0:
        sum_left += arr[row_left_start][col_start]
        sum_right += arr[row_r_start][col_start]
        row_left_start += 1
        col_start += 1
        row_r_start -= 1
        result = sum_right - sum_left
        if sum_left > sum_right:
            result = sum_left - sum_right
        length -= 1
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
