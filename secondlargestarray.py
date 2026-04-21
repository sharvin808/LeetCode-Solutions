arr = [1,2,4,5,7,7,6]
largest = arr[0]
secondlargest = -1
for i in arr:
    if i > largest:
        secondlargest = largest
        largest = i
    elif i < largest and i > secondlargest:
        secondlargest = i
print(largest)
print(secondlargest)
#for i in arr:
 #   if (i > secondlargest)and(i != largest):
  #      secondlargest = i
#print(secondlargest)