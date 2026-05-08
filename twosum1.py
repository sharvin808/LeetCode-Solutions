#brute force method for two sum
#the output can be displayed in two ways either in yes/no or returning the index value
arr = [2,6,5,8,11]
target = 14
for i in range(len(arr)):
    for j in range(i,len(arr)):
        if arr[i]+arr[j] == target:
            print("There is a two sum in the array of target")
            print("The two sum in array is at",i,"and",j)


