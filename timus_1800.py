import math as m

l, h, w = map(float, input().split())

if l / 2 > h:
    print("butter")
else:
    angle = m.sqrt((2 * h - l) / 981) * w / 60
    angle -= int(angle)
    if (angle > 0.25) and (angle < 0.75) and (2 * h - l > 0.0):
        print("bread")
    else:
        print("butter")