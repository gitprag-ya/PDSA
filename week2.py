"""﻿
Write a Python function binarySearchIndexAndComparisons(L, k) that accepts a list L sorted in ascending order and an integer k and returns a tuple (True/False, numComparisons). The first part of this tuple will be True if integer k is present in list L, False otherwise. The second part of the tuple is an integer which gives the number of elements in L that are actually compared to k while searching k in the list L using binary search.
For consistency use (left+right)//2 to calculate the middle index.
Example:
For given L and k, your function should return as mentioned in the table below.
L = [2, 6, 8, 11, 17, 23, 33, 44, 46, 50, 65], list is same for all examples below.
k = 11 Return (True, 3)
k = 23 Return (True, 1)
k = 100 Return (False, 4)"""
def binarySearchIndexAndComparisons(l, k):
    left = 0
    right = len(l)-1
    ct = 0
    if l == []:
        return (False, 1)
    while left<=right:
        mid = (left + right)//2
        ct = ct + 1
        if l[mid]==k:
            return(True, ct)
        if l[mid]>k:
            right = mid-1
        if l[mid]<k:
            left = mid+1
    return (False, ct)
