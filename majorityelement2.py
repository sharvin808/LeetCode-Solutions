#better soln for this using hashing

nums = [2,3,2,3,2,1,2]
freq = {}
major = len(nums)//2
for num in nums:
    if num in freq:             #/
        freq[num] += 1          #/   #freq[num] = freq.get(num,0)+1
    else:                       #/  #instead we can do this way
        freq[num] = 1           #/

    if freq[num] > major:
        print("Majority Element is:",num)
        break
    
