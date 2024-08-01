def climb_stair(n):

    if n == 0:
        return 1
    elif n<0:
        return 0
    else:
        return climb_stair(n-1)+climb_stair(n-2)
    
print(climb_stair(5))
    

     