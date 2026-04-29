arr = [1,1,0,1,1,1,1,0,1,1]
cons = 0
max = 0
for i in range(len(arr)):
    if arr[i] == 1:
        cons += 1
        if cons > max:
            max = cons
    else:
        cons = 0
print(max) 