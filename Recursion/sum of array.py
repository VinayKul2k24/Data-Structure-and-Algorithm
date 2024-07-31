def sum(arr,n):
    if n == 0:
        return 0
    else:
        return sum(arr, n-1) + arr[n-1]
arr1 = [1,2,3,4,5]
print(sum(arr1,len(arr1)))
    