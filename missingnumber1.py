#sum soln
arr = [1,2,3,5,6]
n = 6
sum = n*(n+1)/2
s2 = 0
for i in range(n-1):
    s2 += arr[i]
print(sum - s2)

