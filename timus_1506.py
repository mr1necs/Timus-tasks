n, k = map(int, input().split())
mlist = [int(x) for x in input().split()]
x = k
point = n
for j in range(n // x + 1 if n % x != 0 else n // x):
    i = x - k
    count = 0
    while i < n:
        print(f"{mlist[i]:4d}", end='')
        i += n // x + 1 if n % x != 0 else n // x
    print("")
    k -= 1
