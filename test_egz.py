""" HACKERRANK """

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumPeople function below.
def maximumPeople(p, x, y, r):
    
    tab_p=[None]*len(max(x,y))
    
    # Return the maximum number of people that will be in a sunny town after removing exactly one cloud.

if __name__ == '__main__':
    """ fptr = open(os.environ['OUTPUT_PATH'], 'w') """

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    x = list(map(int, input().rstrip().split()))

    m = int(input())

    y = list(map(int, input().rstrip().split()))

    r = list(map(int, input().rstrip().split()))

    result = maximumPeople(p, x, y, r)

    print(result)
    """ fptr.write(str(result) + '\n')

    fptr.close() """