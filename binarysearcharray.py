arr = [1,2,3,4,5,6,7,8,9]
target = 8
left = 0
right = len(arr) - 1
while left <= right:
    mid = (left+right)//2
    if arr[mid] == target:
        print("Found at index:",mid)
        break
    elif target > arr[mid]:
        left = mid + 1
    else:
        right = mid - 1
