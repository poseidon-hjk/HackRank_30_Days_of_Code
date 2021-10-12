#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    arr_sum = 0
    res = []
    for i in range(0, 4):
        for j in range(0, 4):
            arr_sum += arr[i][j]
            arr_sum += arr[i][j + 1]
            arr_sum += arr[i][j + 2]

            arr_sum += arr[i + 1][j + 1]

            arr_sum += arr[i + 2][j]
            arr_sum += arr[i + 2][j + 1]
            arr_sum += arr[i + 2][j + 2]

            res.append(arr_sum)
            arr_sum = 0
    print(max(res))