def sum(a):
    n = len(a)
    if n==1:
        return a[0]
    if a[0]>a[1]:
        mini = a[1]
        maxi = a[0]
    else:
        mini = a[0]
        maxi = a[1]
    for i in range(2,n):
        if a[i] > maxi:
            a[i] = maxi
        elif a[i] < mini:
            a[i] = mini
    return maxi + mini
a = [-2,1,-4,5,3]
print(sum(a))
     