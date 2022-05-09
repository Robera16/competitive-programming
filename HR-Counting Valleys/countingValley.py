#!/bin/python3

import math
import os
import random
import re
import sys


def countingValleys(steps, path):
    counter=valley=0
    for i in path:
        prev=counter
        if i=="U":
            counter+=1
        else:
            counter-=1
        if prev==-1 and counter==0:
            valley+=1
    return valley
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
