def f1(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return f1(n-1) + f1(n-2)
    
