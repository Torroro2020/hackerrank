#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    cnt1 = 0
    cnt2 = 0
    book = [i for i in range(1, n + 1)]
    pages = (book[i:i + 2] for i in range(1, len(book), 2))
    pages_book = list(pages)
    pages_book = [[1]] + pages_book

    for j in reversed(pages_book):
        if p in j:
            break
        cnt2 += 1

    for i in range(len(pages_book)):
        if p in pages_book[i]:
            break
        cnt1 += 1

    if cnt1 < cnt2:
        return cnt1
    else:
        return cnt2


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
