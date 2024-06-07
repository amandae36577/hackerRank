#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
# The rating for Alice's challenge is the triplet a = (a[0], a[1], a[2]), 
# and the rating for Bob's challenge is the triplet b = (b[0], b[1], b[2]).
#
#The task is to find their comparison points by comparing a[0] with b[0], a[1] with b[1], and a[2] with b[2].
#
# If a[i] > b[i], then Alice is awarded 1 point.
# If a[i] < b[i], then Bob is awarded 1 point.
# If a[i] = b[i], then neither person receives a point.
# Comparison points is the total points a person earned.

Given a and b, determine their respective comparison points.
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    results = [0, 0]
    index = len(a) - 1
    while index >= 0:
        if a[index] > b[index]:
            results[0] = results[0] + 1
        elif a[index] < b[index]:
            results[1] = results[1]+ 1
        index = index - 1
    return results


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
