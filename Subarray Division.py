#!/bin/python3

import math
import os
import random
import re
import sys


def birthday(s, d, m):
    cnt = 0
    for i in range(n-1):
        sum_num = 0
        print('До внутр цикла: ', sum_num)
        for y in range(m):
            sum_num += s[i+y]
            print('После увеличения значения: ', sum_num)
        if sum_num == d:
            cnt += 1
    return cnt







n = int(input().strip())

s = list(map(int, input().rstrip().split()))

dm = input().rstrip().split()

d = int(dm[0])

m = int(dm[1])

result = birthday(s, d, m)

print(result)
