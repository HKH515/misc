n, p = [int(i) for i in input().split()]

for i in range(1, n):
    for j in range(1, p):
        if i**j % p == n:
            print("%s**%s mod %s = %s" % (i, j, p, n))
