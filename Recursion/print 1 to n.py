def print_num(n):
    #base condtion
    if n>0:
        print_num(n-1)
        print(n)
print_num(6)
