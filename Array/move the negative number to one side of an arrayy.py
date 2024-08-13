class solution:
    def negative_num(arr):
        j = 0
        for i in range(0,len(arr)):
            if arr[i]<0:
                temp = arr[i]
                arr[i]=arr[j]
                arr[j]=temp
                j+=1
        return arr 
    print(negative_num([-6,3,4,5,-1,-4],))