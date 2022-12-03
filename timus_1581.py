n = int(input())
mat = list(map(str, (input() + ' END').split()))

count = 1
for i in range(n):
    if mat[i] == mat[i + 1]:
        count += 1
    else:
        print(count, mat[i], end = " ")
        count = 1