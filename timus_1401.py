def fill(n, x, y, hx, hy):
    global count
    if n == 2:
        for i in range(2):
            for j in range(2):
                if not (x + i == hx and y + j == hy):
                    table[x + i][y + j] = int(count / 3)
                    count += 1
        return
    else:
        for i in range(2):
            for j in range(2):
                if x + i * int(n / 2) <= hx < x + i * int(n / 2) + int(n / 2) and y + j * int(
                        n / 2) <= hy < y + j * int(n / 2) + int(n / 2):
                    fill(int(n / 2), x + i * int(n / 2), y + j * int(n / 2), hx, hy)
                else:
                    fill(int(n / 2), x + int(i * n / 2), y + int(j * n / 2), x + int(n / 2) - 1 + i,
                            y + int(n / 2) + j - 1)

    for i in range(2):
        for j in range(2):
            if x + int(i * n / 2) > hx or hx >= x + (i + 1) * int(n / 2) or y + int(j * n / 2) > hy or hy >= y + (
                    j + 1) * int(n / 2):
                table[x + int(n / 2) - 1 + i][y + int(n / 2) - 1 + j] = int(count / 3)
                count += 1


N = int(input())
px, py = map(int, input().split())
s = 2 ** N

table = [0] * s
for i in range(s):
    table[i] = [0] * 512

count = 3
fill(s, 0, 0, px - 1, py - 1)


for i in range(s):
    for j in range(s):
        print(table[i][j], end=" ")
    print()
