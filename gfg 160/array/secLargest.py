

def secLargest(arr):
  n = len(arr)
  arr.sort()
  for i in range(n-2, -1, -1):
    if arr[i] != arr[n-1]:
      return arr[i]
    
  return -1

arr = [12, 35,1, 10, 34, 25]
print(secLargest(arr))
