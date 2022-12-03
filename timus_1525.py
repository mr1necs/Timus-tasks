n, m, k = map(int, input().split())
s = input()
maxR, maxL, maxB, maxF, maxD, maxU = 0, 0, 0, 0, 0, 0
x, y, z = 0, 0, 0

for elem in s:
    if elem == 'u':
        z += 1
        maxU = max(maxU, z)
    if elem == 'd':
        z -= 1
        maxD = min(maxD, z)
    if elem == 'r':
        x += 1
        maxR = max(maxR, x)
    if elem == 'l':
        x -= 1
        maxL = min(maxL, x)
    if elem == 'f':
        y += 1
        maxF = max(maxF, y)
    if elem == 'b':
        y -= 1
        maxB = min(maxB, y)

x = maxR - maxL if maxR - maxL <= (n - 1) else n - 1
y = maxF - maxB if maxF - maxB <= (k - 1) else k - 1
z = maxU - maxD if maxU - maxD <= (m - 1) else m - 1
print((n - x) * (m - z) * (k - y))