#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the birthday function below.
def birthday(s, d, m):
    f = 0
    if m == 1 and sum(s) == d:
        return 1

    for i in range((n - m) + 1):
        subarray, a = 0, 0

        while subarray != m:
            a += s[i]
            i += 1
            subarray += 1

        if a == d:
            f += 1
    return f


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()