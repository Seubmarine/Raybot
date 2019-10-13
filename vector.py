from math import sqrt


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, vector2):
        return Vector2(self.x + vector2.x, self.y + vector2.y)

    def __sub__(self, vector2):
        return Vector2(self.x - vector2.x, self.y - vector2.y)

    def delta_velocity(self, vector2, dt):
        self.x += vector2.x * dt
        self.y += vector2.y * dt

    def __mul__(self, other):
        if type(other) == type(self):
            return Vector2(self.x * other.x, self.y*other.y)
        elif type(other) in (int, float):
            return Vector2(self.x * other, self.y * other)

    def __truediv__(self, other):
        if type(other) == type(self):
            return Vector2(self.x / other.x, self.y / other.y)
        elif type(other) in (int, float):
            return Vector2(self.x / other, self.y / other)

    def __floordiv__(self, other):
        if type(other) == type(self):
            return Vector2(self.x // other.x, self.y // other.y)
        elif type(other) in (int, float):
            return Vector2(self.x // other, self.y // other)
    
    def replace(self, vector2):
        self.x = vector2.x
        self.y = vector2.y

    def magnitude(self):
        return self.x*self.x + self.y*self.y

    def sqrtMagnitude(self):
        return sqrt(self.magnitude())

    def normalize(self):
        m = self.sqrtMagnitude()
        if m != 0:
            return self / m

    def reverse(self):
        return Vector2(self.x * -1, self.y * -1)

    def limit(self, number):
        if self.y <= number:
            self.y = number

    def normalizefromvector(self, vector2):
        self -= vector2
        return self.normalize()

    def distancefromvector(self, vector2):
        self -= vector2
        return self.magnitude()

    def returned(self, vector2):
        return vector2.x, vector2.y

    def collide(self, vector2):
        return (self.x - vector2.x) ** 2 + (self.y - vector2.y)**2

    def up(self, velocity):
        self.y -= velocity

    def down(self, velocity):
        self.y += velocity

    def left(self, velocity):
        self.x -= velocity

    def right(self, velocity):
        self.x += velocity

    def __int__(self):
        # self.x = int(self.x)
        # self.y = int(self.y)
        return Vector2(int(self.x), int(self.y))

    def __repr__(self):
        return str('%s %s'%(self.x, self.y))