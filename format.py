def format_number(n):
    n = round(n, 3)

    stroka = str(n)

    dot = False
    for i in stroka:
        if i == '.':
            dot = True
            break

    if dot:
        celoe = ''
        drob = ''
        after_dot = False
        for i in stroka:
            if i == '.':
                after_dot = True
            elif not after_dot:
                celoe = celoe + i
            else:
                drob = drob + i

        while len(drob) < 3:
            drob = drob + '0'
    else:
        celoe = stroka
        drob = '000'

    probel = ''
    c = 0
    obratno = ''
    for i in celoe:
        obratno = i + obratno

    for i in obratno:
        if c > 0 and c % 3 == 0:
            probel = ' ' + probel
        probel = i + probel
        c = c + 1

    res = probel + ' .' + drob

    while len(res) < 30:
        res = '*' + res + '*'

    if len(res) > 30:
        res = res[:30]

    return res

