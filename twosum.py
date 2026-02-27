def two_sum1(n, a):
    n = len(n)
    for i in range(n):
        for j in range(i + 1, n):
            if n[i] + n[j] == a:
                return [i, j]
    return []

def two_sum2(n, a):
    for i in range(len(n)):
        for j in range(i + 1, len(n)):
            if n[i] > n[j]:
                n[i], n[j] = n[j], n[i]

    l = 0
    r = len(n) - 1
    while l < r:
        sum = n[l] + n[r]

        if sum == a:
            return [n[l], n[r]]
        elif sum < a:
            l += 1
        else:
            r -= 1

    return []
