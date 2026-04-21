arr = [1,2,4,5,7,7,6]
smallest = arr[0]
secondsmallest = max(arr)
for i in arr:
    if i < smallest:
        secondsmallest = smallest
        smallest = i
    elif i != smallest and i < secondsmallest:
        secondsmallest = i
print(smallest)
print(secondsmallest)
