def fill(n, x, y, xhole, yhole):
    global count
    if n == 2:
        for i in range(2):
            for j in range(2):
                if not (x + i == xhole and y + j == yhole):
                    table[x + i][y + j] = int(count / 3)
                    count += 1
        return
    else:
        for i in range(2):
            for j in range(2):
                if x + i * int(n / 2) <= xhole < x + i * int(n / 2) + int(n / 2) and y + j * int(
                        n / 2) <= yhole < y + j * int(n / 2) + int(n / 2):
                    fill(int(n / 2), x + i * int(n / 2), y + j * int(n / 2), xhole, yhole)
                else:
                    fill(int(n / 2), x + int(i * n / 2), y + int(j * n / 2), x + int(n / 2) - 1 + i, y + int(n / 2) + j - 1)

    for i in range(2):
        for j in range(2):
            if x + int(i * n / 2) > xhole or xhole >= x + (i + 1) * int(n / 2) or y + int(j * n / 2) > yhole or yhole >= y + (j + 1) * int(n / 2):
                table[x + int(n / 2) - 1 + i][y + int(n / 2) - 1 + j] = int(count / 3)
                count += 1


N = int(input())
xbox, ybox = map(int, input().split())
N = 2 ** N

table = [0] * N
for i in range(N):
    table[i] = [0] * 512

count = 3
fill(N, 0, 0, xbox - 1, ybox - 1)

for i in range(N):
    for j in range(N):
        print(table[i][j], end=" ")
    print()
