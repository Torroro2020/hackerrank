#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the breakingRecords function below.
def breakingRecords(scores):
    num_max, num_min, cnt_suc, cnt_fail = scores[0], scores[0], 0, 0

    for i in range(0, n-1):
        if scores[i] < scores[i + 1] and num_max < scores[i + 1]:
            num_max = scores[i + 1]
            cnt_suc += 1
        elif scores[i + 1] < scores[i] and scores[i + 1] < num_min:
            num_min = scores[i + 1]
            cnt_fail += 1

        print(cnt_suc, cnt_fail)

    return cnt_suc, cnt_fail


n = int(input())
scores = list(map(int, input().rstrip().split()))
result = breakingRecords(scores)

print(result)
