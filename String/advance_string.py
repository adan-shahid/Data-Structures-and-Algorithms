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
