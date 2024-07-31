#reverse the given list using recuretion
def printnum(arr,index):
    #base conditon
    if index>=len(arr):
        return     
    #logic condtion
    printnum(arr,index+1)
    #Recursive call
    print(arr[index])
lst = [int(x) for x in input('enter a number:').split(',')]
printnum(lst,0)