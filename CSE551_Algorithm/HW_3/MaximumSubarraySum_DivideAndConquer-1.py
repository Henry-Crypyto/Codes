#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sys import maxsize

arr = [15, 13, 8, 14, 12, 9, 10, 15, 9]
ans = -maxsize - 1

def max_crossing_sum(arr, low, mid, high):
    
    left_min = arr[mid]
    for i in range(mid - 1, low - 1, -1):
        left_min = min(left_min, arr[i])
    
    
    right_max = arr[mid + 1]
    for j in range(mid + 2, high + 1):
        right_max = max(right_max, arr[j])

    return right_max - left_min

def max_profit_recursive(arr, low, high):
    if low >= high:
        return 0
    
    mid = (low + high) // 2
    left_profit = max_profit_recursive(arr, low, mid)
    right_profit = max_profit_recursive(arr, mid + 1, high)
    cross_profit = max_crossing_sum(arr, low, mid, high)

    return max(left_profit, right_profit, cross_profit)

ans = max_profit_recursive(arr, 0, len(arr) - 1)
print("Max Profit (O(n log n)): ", ans)