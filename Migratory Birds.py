#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    new_arr = []
    dict_sample = {}
    for elem in arr:
        if elem not in new_arr:
            dict_sample[elem] = 1
            new_arr.append(elem)
        elif elem in new_arr:
            dict_sample[elem] += 1
    max_value = max(dict_sample.values())
    final_dict = {k: v for k, v in dict_sample.items() if v == max_value}
    return min(final_dict.keys())




arr_count = int(input().strip())

arr = list(map(int, input().rstrip().split()))

result = migratoryBirds(arr)

print(result)


