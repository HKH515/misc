def threesum(a):
    a = sorted(a)
    n = len(a)
    count = 0
    for i in range(n):
        j = i+1
        k = n-1
        while j < k:
            sm = a[i] + a[j] + a[k]
            if sm == 0:
                count += 1
                j += 1
                k -= 1
            if sm < 0:
                j += 1
            if sm > 0:
                k -= 1
    return count
                 
a = [int(i) for i in input().split()]
print(threesum(a))
