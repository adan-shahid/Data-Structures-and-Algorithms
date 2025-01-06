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


# Maximum Sum Sublist or Subarray

    # Naive Approach

def maxSum1(l,n):
    res = l[0]
    for i in range(0,n):
        curr = 0
        for j in range(i,n):
            curr = curr + l[j]
            res = max(res,curr)
    return res

    # Efficient Approach

def maxSum2(l,n):
    res = l[0]
    maxEnding = l[0]
    for i in range(1,n):
        maxEnding = max(maxEnding+l[i], l[i])
        res = max(maxEnding,res)
    return res

# Maximum Circular Sum Subarray or Sublist

    # Naive Approach

def maxCircularSum1(l,n):
    res = l[0]
    for i in range(0,n):
        curr_max = l[i]
        curr_sum = l[i]

        for j in range(1,n):
            index = (i+j)%n
            curr_sum += l[index]
            curr_max = max(curr_max, curr_sum)
        res = max(res, curr_max)
    return res


    # Efficient Approach

def normalMaxSum(l,n):
    res = l[0]
    maxEnding = l[0]
    for i in range(1,n):
        maxEnding = max(maxEnding+l[i], l[i])
        res = max(maxEnding,res)
    return res

def overallMaxSum(l,n):
    max_normal = normalMaxSum(l,n)

    if max_normal < 0:
        return max_normal

    l_sum = 0
    for i in range(0,n):
        l_sum += l[i]
        l[i] = -l[i]

    max_circular = l_sum + normalMaxSum(l,n)

    return max(max_circular,max_normal)

# Find the majority element in the list
# Majority element ----> that element should appear more than n/2 times,
#                       Not exactly n/2, it should be more


    # Naive Method

def findMajority1(l,n):
    for i in range(n):
        count = 1
        for j in range(i+1,n):
            if l[i] == l[j]:
                count +=1
        if count > n/2:
            return i
    return -1

    # Efficient Method

def findMajority2(l,n):
    res = 0
    count = 0

    # finding a candidate

    for i in range(1,n):
        if l[res] == l[i]:
            count += 1
        else:
            count -=1
        if count == 0:
            res = i
            count = 1
    # Check if a candidate is actually a majority

    count = 0
    for i in range (0,n):
        if l[res] == l[i]:
            count += 1
    if count <= (n//2):
        res = -1
    return res

# Maximum group flips to make same

def printGroups(l,n):
    for i in range(1,n):
        if (l[i] != l[i-1] ):
            if ( l[i] != l[0]  ):
                print('From', i, 'to', end =" ")
            else:
                print(i-1)
            
    if (l[n-1] != l[0]):
        print(n-1)

# find the Maximum sum of 'k' consective elements

    # Naive Approach

def maxKSum1(l,k):
    n = len(l)
    res = float("-inf")
    i = 0
    while (i+k-1 < n):
        curr = 0
        for j in range(k):
            curr += l[i+j]
        res = max(curr,res)
        i+=1
    return res

    # Efficient Approach --> Sliding Window Technique

def kMaxSum2(l,k):
    curr = 0
    for i in range(k):
        curr += l[i]
    res = curr
    for i in range(k,len(l)):
        curr = curr + l[i] - l[i-k]
        res = max(res,curr)
    return res

# Subarray with Given Sum

    # Naive Approach

def isSubSum1(l,sum):
    for i in range(len(l)):
        curr = 0
        for j in range(i,len(l)):
            curr += l[j]
            if (curr == sum):
                return True
    return False

    # Efficient Approach

def isSubSum2(l,sum):
    s,curr = 0,0
    for e in range(len(l)):
        curr += l[e]
        while (curr > sum):
            curr -= l[s]
            s += 1
        if (curr == sum):
            return True

    return False

# Prefix Sum Technique --> given a fixed list and multiple range sum queries
                        # how to answer the queries effciently
# Important interview question

    # Naive Solution

def getSum1(l,r):
    res = 0
    for i in range(l,r+1):
        res += l[i]
    return res

    # Efficient Solution
l = [2,8,3,9,6,5,4]
n = len(l)
pSum = [None] * n
pSum[0] = l[0]
for i in range(1,n):
    pSum[i] = pSum[i-1] +l[i]

def getSum2(l,r):
    if l == 0:
        return pSum[r]
    else:
        return pSum[r] - pSum[l-1]


# Equilibrium point --> if the list has equilibrium point or not
# A point is called equilibrium point, if sum of elements before it and sum
# elements after it is the same.

    # Naive Solution
def ePoint1(l):
    n = len(l)
    for i in range(n):
        ls, rs = 0, 0
        for j in range(i):
            ls += l[j]
        for k in range(i+1,n):
            rs += l[k]
        if (ls == rs):
            return True
    return False

    
    # Efficient Solution

def ePoint2(l):
    rs = sum(l)
    ls = 0
    for i in range(len(l)):
        rs -= l[i]
        if (ls == rs):
            return True
        ls += l[i]
    return False

# Maximum appearing element in ranges

    # Naive Solution

def maxAppear1(left, right):
    freq = [0] * 100
    for i in range(len(l)):
        for j in range(left[i], right[i]+1):
            freq[j] += 1
    
    return freq.index(max(freq))

    # Efficient Solution

def maxAppear2(left,right):
    freq = [0] * 101
    for i in range(len(left)):
        freq[left[i]] += 1
        freq[right[l]+1] -= 1

    for i in range(1,100):
        freq[i] = freq[i] + freq[i-1]

    return freq.index(max(freq))


l = [-8,7,6]
d = 3
print(maxCircularSum1(l,d))

