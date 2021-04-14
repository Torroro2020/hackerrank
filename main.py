#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    minNumberOfM = min(b)
    answers = ['Кратное', 'Некратное']
    findListNumber = []
    resultListNumber = []

    for i in range(1, minNumberOfM + 1):
        cnt_for_a = 0
        for element in range(n):
            if i % a[element] == 0:
                answer = answers[0]
                cnt_for_a += 1
            else:
                answer = answers[1]
        if cnt_for_a == n:
            findListNumber.append(i)



    for i in findListNumber:
        cnt_for_b = 0
        for element in b:
            if element % i == 0:
                answer = answers[0]
                cnt_for_b += 1
            else:
                answer = answers[1]
        if cnt_for_b == m:
            resultListNumber.append(i)

    return len(resultListNumber)


n = 2
m = 3

arr = [2, 4]
brr = [16, 32, 96]

total = getTotalX(arr, brr)
print(total)