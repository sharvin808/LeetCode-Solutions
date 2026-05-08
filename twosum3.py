#optimal solution for two sum using 2 pointer technique
# the solution is found by sorting the array so the index provided would be the newly sorted array's

arr = [2,6,5,8,11]
new_arr = sorted(arr)
target = 14
left = 0
right = len(new_arr)-1
while left < right:
    current = new_arr[left]+new_arr[right]
    if current == target:
        print("The two sum solution in array is at:",left,right)
        break
    elif current < target:
        left += 1
    else:
        right -= 1

#this solution is given using sorting but by returning the original index by storing the originl index 
#on another array it would take more time complexity
arr = [2,6,5,8,11]
target = 14
new_arr = []
for i in range(len(arr)):
    new_arr.append((arr[i],i))
new_arr.sort()
left = 0
right =len(new_arr)-1
while left < right:
    current = new_arr[left][0] + new_arr[right][0]
    if current == target:
        print("The two sum is solved at index:",new_arr[left][1],new_arr[right][1])
        break
    elif current < target:
        left += 1
    else:
        right -= 1



