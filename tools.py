class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector2(self.x * other, self.y * other)

    def __truediv__(self, other):
        return Vector2(self.x / other, self.y / other)
    
    def __floordiv__(self, other):
        return Vector2(self.x // other, self.y // other)

    def magnitude(self):
        return (self.x**2 + self.y**2)**0.5
    def to_array(vector):
        return [vector.x, vector.y]
    def normalize(self):
        length = self.magnitude()
        return Vector2(self.x / length, self.y / length)
