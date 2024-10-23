#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sys import maxsize

arr = [15, 13, 8, 14, 12, 9, 10, 15, 9]
ans = -maxsize - 1


min_price = arr[0]

for i in range(1, len(arr)):
    profit = arr[i] - min_price
    if profit > ans:
        ans = profit
    if arr[i] < min_price:
        min_price = arr[i]

print("Max Profit (O(n)): ", ans)
