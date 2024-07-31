def printnum(arr,index):
    #base conditon
    if index>=len(arr):
        return
    #logic condtion
    print(arr[index])
    #Recursive call
    printnum(arr,index+1)
lst = [int(x) for x in input('enter a number').split(',')]
printnum(lst,0)