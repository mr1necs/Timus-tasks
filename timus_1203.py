n = int(input())
time = [[int(x) for x in input().split()] for i in range(n)]
count, endl = 0, 0

time.sort(key=lambda x: x[1])

for data in time:
    if endl < data[0]:
        endl = data[1]
        count += 1
print(count)
