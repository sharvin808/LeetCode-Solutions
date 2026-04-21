arr = [1,2,3,4,5,7,7,6]
for i in range(len(arr)-1):
    if arr[i] <= arr[i+1]:
        a = 1
    else:
        a = 0
    
if a == 1:
    print("The array is sorted")
else:
    print("The array is not sorted")