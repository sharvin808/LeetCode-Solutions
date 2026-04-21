arr = [5,10,15,20]
total = 0
for i in arr:
    total += i
print(total)
max = arr[0]
for i in arr:
    if i > max:
        max = i
print(max)
min = arr[0]
for i in arr:
    if i < min:
        min = i
print(min)
target = 15
for i in range(len(arr)):
    if arr[i] == 15:
        print(i)

arr1 = [1,2,3,4]
left = 0
right = len(arr1)-1
while left < right:
    arr1[left],arr1[right] = arr1[right],arr1[left]
    left += 1
    right -= 1
print(arr1)