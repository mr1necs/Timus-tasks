n = [int(x) for x in input().split()]

min_value = 0
for i in n:
    min_value += i
if n[8] == 10 and n[9] > 20:
    min_value += 10

max_point = [1] * 10
max_value = 0

for i in range(7):
    if n[i] == 10:
        max_point[i+1] += 1
        if n[i+1] == 10:
            max_point[i + 2] += 1

if n[7] == 10:
    if n[8] == 10:
        max_value += 10
        if n[9] > 10:
            max_value += 10

if n[8] == 10:
    if n[9] >= 20:
        max_value += 20
    elif n[9] > 10:
        max_value += 10 + n[9] % 10

for i in range(10):
    max_value = max_value + max_point[i] * n[i]

print(min_value, max_value)
