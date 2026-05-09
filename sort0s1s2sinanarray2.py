#optimal soln for sort array of 0s 1s 2s using Dutch National flag Algorithm
#Dutch NAtional Flag Algorithm:
#[0 .... low-1] == 0
#[low .... mid-1] == 1
#[mid .... high] == unsorted arrays
#[high+1 .... n-1] == 2
# so we are considering our array is in b/w [mid ... high]

arr = [0,1,1,0,0,1,0,0,0,2,2,1,2]
low = 0
mid = 0
high = len(arr)-1
while mid <= high:
    if arr[mid] == 0:
        arr[low],arr[mid] = arr[mid],arr[low]
        low += 1
        mid += 1
    elif arr[mid] == 1:
        mid += 1
    else:
        arr[mid],arr[high] = arr[high],arr[mid]
        high -= 1
print(arr)