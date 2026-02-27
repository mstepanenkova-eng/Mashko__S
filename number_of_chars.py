def f(s):
    c = {}
    for i in s:
        c[i] = c.get(i, 0) + 1
    
    return c
