n, a, b = map(int, input().split())
ax = [0] * (n + 1)
ay = [0] * (n + 1)
ax[0], ax[1] = 1, 1
ay[0], ay[1] = 1, 1
M = 1e9 + 7

for i in range(2, n + 1):
    ax[i] = (int((sum(ay[i - 1:i - a:-1]) + ay[i - a]) % M) if i - a > 0 else int(sum(ay[i - 1:0:-1]) + ay[0] % M))
    ay[i] = (int((sum(ax[i - 1:i - b:-1]) + ax[(i - b)]) % M) if i - b > 0 else int((sum(ax[i - 1:0:-1]) + ax[0]) % M))

print(int((ax[n] + ay[n]) % M))