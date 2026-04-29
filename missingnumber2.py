#xor soln #error
arr = [1,2,3,5,6]
n = 6
xor1 = 0
for i in range(n):
    xor1 ^= i
xor2 = 0 
for j in range(n-1):
    xor2 ^= arr[j]
print(xor1^xor2)