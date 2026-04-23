arr1 = [1,1,2,3,4,5]
arr2 = [2,3,4,4,5,6]
intersect = []
i,j = 0,0
while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            if len(intersect) == 0 or intersect[-1] != arr1[i]:
                intersect.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
             i += 1
        else:
            j += 1
print(intersect)
