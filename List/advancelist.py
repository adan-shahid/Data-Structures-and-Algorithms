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



# Stock Buy and Sell

def maxProfit(price,n):
    profit = 0
    for i in range(1,n):
        if price[i] > price[i-1]:
            profit += price[i] - price[i-1]
    
    return profit


# Trapping Rain Water

    # Naive Solution

def getWater1(l,n):
    res = 0
    for i in range(1,n-1):
        lmax = l[i]

        for j in range(0,i):
            lmax = max(lmax,l[j])

        rmax = l[j]

        for j in range(i+1, n):
            rmax = max(rmax,l[j])

        res = res + (min(lmax,rmax) - l[i])

    return res


    # Efficient Solution

def getWater2(l,n):
    res = 0
    lmax = [0] * n
    rmax = [0] * n

    lmax[0] = l[0]
    for i in range(1,n):
        lmax = max(l[i], lmax[i-1])

    rmax[n-1] = l[n-1]
    for i in range(n-2, -1, -1):
        rmax = max(l[i], rmax[i+1])

    for i in range(1, n-1):
        res = res + (min(lmax[i], rmax[i])-l[i])

    return res


# Maximum Length SUblist --> That has alternating enev/odd  element

    # Naive Approach

def maxEvenOdd1(l,n):
    res = 1
    for i in range(0,n):
        curr = 1
        for j in range(i+1,n):
            if (l[j] %2 == 0 and l[j-1] % 2 != 0 ) or (l[j] % 2 != 0 and l[j-1]%2 == 0):
                curr += 1
            else:
                break

        res = max(res,curr)
    return res

    # Efficient Solution

def maxEvenOdd2(l,n):
    res = 1
    curr= 1
    for i in range(1,n):
        if (l[i] %2 == 0 and l[i-1] % 2 != 0 ) or (l[i] % 2 != 0 and l[i-1]%2 == 0):
            curr += 1
            res = max(res,curr)
        else:
            curr = 1

    return res


l = [1,2,3,4,5,6]
d = 6
print(maxProfit(l,d))

