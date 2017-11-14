def ECPoints(A, B, p):
    """
    Prints all points on the elliptic curve
    E : Y^2 = X^3 + AX + B in the field mod 7
    """

    points = [(0, 0)]

    for x in range(p):
        rhs = (x**3 + A*x + B) % p
        for y in range(p):
            if y**2 % p == rhs:
                points.append((x, y))
    return points

A, B, p = [int(i) for i in input().split()]
print(ECPoints(A, B, p))
