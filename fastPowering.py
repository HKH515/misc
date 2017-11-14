g, A, N = [int(i) for i in input().split()]

prod = 1
last = g
for i in range(len(bin(A)[2:])):
    a = last**2
    a = a % N
    if bin(A)[2:][::-1][i] == '1':
        prod *= last
    last = a
print(prod % N)