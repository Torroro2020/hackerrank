#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the repeatedString function below.
def repeatedString(s, n):
    if n % len(s) == 0:
        return s.count('a') * (n // len(s))
    else:
        return (s.count('a') * (n // len(s))) + s[0:n % len(s)].count('a')





n = 10
s = 'aba'
result = repeatedString(s, n)
print(result)
