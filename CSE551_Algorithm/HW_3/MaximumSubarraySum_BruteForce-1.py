#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sys import maxsize

arr = [15, 13, 8, 14, 12, 9, 10, 15, 9]
ans = -maxsize - 1


n = len(arr)
for i in range(n):
    for j in range(i + 1, n):
        profit = arr[j] - arr[i]
        if profit > ans:
            ans = profit

print("Max Profit (O(n^2)): ", ans)