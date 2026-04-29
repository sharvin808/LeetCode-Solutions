#xor soln #error
arr = [1,2,3,5,6]
n = 6
xor1 = 0
for i in range(1,n+1):
    xor1 ^= i
xor2 = 0 
for j in arr:
    xor2 ^= j
print(xor1^xor2)