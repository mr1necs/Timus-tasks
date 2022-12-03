from math import pi, sqrt

count, rad = map(float, input().split())

per = 2 * pi * rad
mat = []

for i in range(int(count)):
    mat.append(list(map(float, input().split())))
mat.append(mat[0])

if count > 1:
    for i in range(int(count)):
        per += sqrt((mat[i + 1][0] - mat[i][0]) ** 2 + (mat[i + 1][1] - mat[i][1]) ** 2)

print(f'{per:0.2f}')