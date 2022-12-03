n = int(input())
mlist = [int(x) for x in input().split()]
mlist.sort()
count = 0
for i in range(n // 2 + 1):
    count += mlist[i] // 2 + 1
print(count)