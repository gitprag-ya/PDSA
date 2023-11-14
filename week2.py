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
