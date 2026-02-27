def f(s):
    
    a = []
    for i in s:
        if i == '(':
            a.append(i)
        elif i == ')':
            if not a:
                return False
            a.pop()
    return len(a) == 0
