#!/usr/bin/python

def geron(a):
    x = 1
    e = 0.0000000000001
    while not (a - e < x ** 2 < a + e):
        x = 1/2 * (x + a / x)

    return x


for i in range(1, 21):
    print(geron(i))

# x[n+1] = 1/2 * (x[n] + a / x[n])
