import math


class get_vector:
    __slots__ = ['x', 'y', 'z']

    def __init__(self, ix=0, iy=0, iz=0):
        self.x = ix
        self.y = iy
        self.z = iz

    def as_tuple(self): return self.x, self.y, self.z
    def __iter__(self): return iter(self.as_tuple())
    def __mul__(self, other): return __class__(self.x * other, self.y * other, self.z * other)
    def __abs__(self): return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
    def __add__(self, other): return __class__(self.x + other.x, self.y + other.y, self.z + other.z)
    def __sub__(self, other): return __class__(self.x - other.x, self.y - other.y, self.z - other.z)
    def __truediv__(self, other): return __class__(self.x / float(other), self.y / float(other), self.z / float(other))
    def vector_mul(self, other): return __class__(self.y * other.z - self.z * other.y, self.z * other.x - self.x * other.z, self.x * other.y - self.y * other.x)
    def sc_dot(self, other): return self.x * other.x + self.y * other.y + self.z * other.z


a, b = map(int, input().split())
v0 = get_vector(0, 0, 0)
x, y, z = map(float, input().split())
v1 = get_vector(x, y, z)
x, y, z = map(float, input().split())
v2 = get_vector(x, y, z)

v = v0 - v1
w = v2 - v1
point = v1 + w * (get_vector.sc_dot(v, w) / (abs(w)**2))
r = point - v0
d = abs((v0 - point))

t = math.acos(min(max(-1.0, (b * b - a * a - d * d) / (-2 * a * d)), 1.0))
s = math.acos(min(max(-1.0, (d * d - a * a - b * b) / (-2 * a * b)), 1.0))

if d > a + b or s < math.pi/2 - 1e-9:
    print("No solution.")
else:
    q = get_vector.vector_mul(w, r) / abs(get_vector.vector_mul(w, r))
    W = r / abs(r) * a * math.cos(t) + q * a * math.sin(t)
    x, y, z = map(float, W)
    print(x, y, z, s)

