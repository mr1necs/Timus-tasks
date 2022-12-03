import math
n, k = map(int, input().split())
if k < n:
    print(math.ceil(n * 2 / k))
else:
    print(2)
