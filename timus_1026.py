n = int(input())
mlist = []
for i in range(n):
    mlist.append(int(input()))
mlist.sort()
mstr = input()
k = int(input())
for i in range(k):
    mstr = int(input())
    mlist.append(mlist[mstr - 1])
for i in range(n, n + k):
    print(mlist[i])