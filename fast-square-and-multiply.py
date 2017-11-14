import math
def sam(N, g, A):
    a = g
    b = 1
    while A > 0:
        if A % 2 == 1:
            b = (b * a) % N
        a = (a*a) % N
        A = math.floor(A/2)
    return b

Ni, gi, Ai = [int(i) for i in input().split()]
print(sam(Ni, gi, Ai))
