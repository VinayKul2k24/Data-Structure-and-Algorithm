arr1 = [1,3,4,2,5,7,8,9,2]
arr1.sort()
for i in range(1,len(arr1)):
        if arr1[i-1]==arr1[i]:
            print(arr1[i])
