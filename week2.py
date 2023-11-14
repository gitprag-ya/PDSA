"""﻿ PPA-1
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


"""PPA-2
Consider a list L containing n integers, where each integer i is in the range [[0, r) that is 0 <= i <r, r<1000 and n>>r (n is much greater than r). Write a Python function sortInRange (L, r) to sort the list L in ascending order. Try to write a solution that runs in O(n + r) asymptotic complexity.
Sample Input:
L: 2, 0, 1, 1, 2, 3, 0, 2, 1, 0, 2, 3, 1, 2
r: 4
Sample Output:
0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3
Note:- In function, no need to return any list, just sort input list `'L' in place."""
def sortInRange(L, r):
    # create a list of r zeros
    count = [0] * r
    # loop through the input list and increment the count of each element
    for x in L:
        count[x] += 1
    # loop through the count list and overwrite the input list with the sorted elements
    i = 0 # index for the input list
    for x in range(r): # loop through the range
        for _ in range(count[x]): # loop through the count of each element
            L[i] = x # assign the element to the input list
            i += 1 # increment the index



