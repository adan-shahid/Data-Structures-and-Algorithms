# Left Rotate by 'd' places

    # Simple Method

def leftRotate1(l,d): ## it take theta (nd) time
    for i in range(0,d):
        l.append(l.pop(0)) # pop operation takes theta(n) time
    return l

    # We can do the same in theta(n) time and O(1) Auxillary space

def leftRotate2(l,d):
    n = len(l)
    reverse(l,0,d-1)
    reverse(l,d,n-1)
    reverse(l,0,n-1)
    return l

def reverse(l,b,e):
    while b < e:
        l[b], l[e] = l[e], l[b]
        b = b + 1
        e = e - 1


# Maximum DIfference between any 2 elements of List.
# Given the list is either sorted or unsorted.

    # Naive Approach

def maxDiff1(l,n):
    res = l[1] - l[0]
    for i in range(0, n-1):
        for j in range(i + 1, n):
            res = max(res, l[j]-l[i])
    return res

    # Efficient Solution

def maxDiff2(l,n):
    res = l[1] - l[0]
    minval = l[0]
    for j in range(1,n):
        res = max(res, l[j] - minval)
        minval = min(l[j], minval)
    return res


l = [1,2,3,4,5,6]
d = 6
print(maxDiff2(l,d))

