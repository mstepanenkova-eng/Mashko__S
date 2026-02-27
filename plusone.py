def plus_one(n):
    for i in range(len(n) - 1, -1, -1):
        if n[i] < 9:
            n[i] += 1
            return n
        else:
            n[i] = 0
    
    return [1] + n
