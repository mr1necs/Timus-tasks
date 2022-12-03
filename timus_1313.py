n = int(input())
screen = []
new = []

for i in range(n):
    screen.append(list(map(int, input().split())))

for i in range(n + 1):
    for j in reversed(range(i)):
        new.append(screen[j][i - j - 1])

for i in range(1, n):
    for j in reversed(range(i, n)):
        new.append(screen[j][i - j - 1])

for i in range(n * n):
    print(new[i],  end = " ")
