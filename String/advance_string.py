# Pattern Searching Algorithms.

    # Using Simple string methods in python

txt = input("Enter the text : \n")
pat = input("Enter the pattern : \n")
pos = txt.find(pat)

while pos >= 0:
    print(pos)
    pos = txt.find(pat, pos+1)

    # Naive pattern Searching Algorithm

def naivePat(txt,pat):
    m = len(pat)
    n = len(txt)
    for i in range(n-m+1):
        j = 0
        while j < m:
            if pat[j] != txt[i+j]:
                break
            j = j + 1
        if j == m:
            print(i, end = "")

    
    # Improved Naive approach for Distinct in Pattern

def distPatSearch(txt,pat):
    m,n = len(pat), len(txt)
    i = 0
    while i <= (n-m):
        for j in range(m):
            if pat[j] != txt[i+j]:
                break
        if j == m:
            print(i, end = " ")
        if j == 0:
            i += 1
        else:
            i += j

# Rabin Karp Algorithm

def RKSearch(pat, txt, q): # q is basically a large prime number(Random)
    m,n = len(pat), len(txt)
    h = 1
    for i in range(1,m):
        h = (h * d) * q

    p, t = 0, 0
    for i in range(m):
        p = (p*d* ord(pat[i])) % q
        t = (t*d* ord(txt[i])) % q

    for i in range(n-m+1):
        if p == t:
            for j in range(m):
                if txt[i+j] != pat[j]:
                    break
                else:
                    j += 1
            if j == m:
                print(i)

        if i < (n-m):
            t = ((d*(t-ord(t*t[i]*h)) + ord(txt[i+m]))) % q
        if t < 0:
            t = t + q

# KMP Algorithm ----> Knuth Morris Pratt Algorithn

        # Constructing LPS Array

def longestPrefixSuffix(s) :
    n = len(s)
    lps = [0] * n   
    l = 0
     
    i = 1
    while (i < n) :
        if (s[i] == s[l]) :
            l = l + 1
            lps[i] = l
            i = i + 1
         
        else :
            if (l != 0) :
                l = lps[l-1]
  
            else :
 
                lps[i] = 0
                i = i + 1
  
    res = lps[n-1]
    if(res > n/2) :
        return n//2
    else :
        return res
