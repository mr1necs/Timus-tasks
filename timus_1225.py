n = int(input())
counter = [0, 2]
if n > 1:
    for i in range(2, n + 1):
        counter.append(counter[i - 1] + counter[i - 2])
print(counter[n])
