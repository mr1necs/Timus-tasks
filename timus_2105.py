L, T, va, vb = map(int, input().split())
n = int(input())
time = [0] * 2
for _ in range(n, 0, -1):
    n -= 1
    type_i, _, d = map(int, input().split())
    time[type_i-1] += d
print(int((va * (T - time[0]) + vb * (T - time[1])) / L))