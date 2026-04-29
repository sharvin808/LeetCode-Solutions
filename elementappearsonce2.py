arr = [1,1,2,3,3,4,4]
maxi = arr[0]
for i in range(len(arr)):
    maxi = max(maxi,arr[i])
freq = [0] * (maxi+1)
for i in range(len(arr)):
    freq[arr[i]] += 1
for i in range(len(arr)):
    if freq[arr[i]] == 1:
        print(arr[i])