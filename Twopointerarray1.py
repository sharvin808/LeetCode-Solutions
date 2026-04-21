arr = [1,2,3,5,6,7,8]
target = 10
left = 0
right = len(arr)-1
while left < right:
    s = arr[left]+arr[right]
    if s == target:
        print("Pair found:",arr[left],arr[right])
        break
    elif s < target:
        left += 1
    else:
        right -= 1
