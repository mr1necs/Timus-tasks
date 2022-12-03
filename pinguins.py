def printer(n,  st):
    pin = ''
    for i in range(n):
        pin += st
    return pin


n = int(input())

print(printer(n, "    _~_    "))
print(printer(n, "   (o o)   "))
print(printer(n, "  /  V  \  "))
print(printer(n, " /(  +  )\ "))
print(printer(n, "   ^^ ^^   "))
