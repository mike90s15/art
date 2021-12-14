#!/urs/bin/env python
def triangle(a):
    b = a - 1
    c = '*'

    for a in range(1, a):
        print(f'\033[{a};{b}H{c}\n', end='')
        b -= 1
        c = c + '**'


print('\033c', end='')
n = 6
triangle(n)
