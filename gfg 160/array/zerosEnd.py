#Solution 1.

# arr = [5, 0, 10, 14, 0, 2,20]
# count = 0
# for i in range(len(arr)):
#   if arr[i] != 0:
#     arr[count], arr[i] =arr[i], arr[count]
#     count += 1
# print(arr)    


#Solution 2

arr = [5, 0, 10, 14, 0, 20]
count = 0
for i in range(len(arr)):
  if arr[i] != 0:
    arr[count] = arr[i]
    count += 1
while count < len(arr):
  arr[count] = 0
  count += 1
  
print(arr)
