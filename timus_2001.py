a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
b1 -= b2
a2, b2 = map(int, input().split())
a1 -= a2
print(a1, b1)
