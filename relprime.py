x, y = [int(i) for i in input().split()]

while y != 0:
    x = x % y
    curX = x
    curY = y
    x = curY
    y = curX
print(x)