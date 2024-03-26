# Vector2D class for operating with vector objects
import math

class Vector2D():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.thresh = 0.000001
        
    def __add__(self, other):
        sum = self.x + other.x
        sum1 = self.y + other.y
        return Vector2D(sum,sum1)

    def __sub__(self, other):
        result = self.x - other.x
        result1 = self.y - other.y
        return Vector2D(result, result1)

    def __neg__(self):
        negative = self.x*(-1)
        negative1 = self.y*(-1)
        return Vector2D(negative, negative1)

    def __mul__(self, scalar):
        product = self.x * scalar.x
        product1 = self.y * scalar.y
        return Vector2D(product,product1)

    def __div__(self, scalar):
        if scalar != 0:
            x = self.x / scalar
            y = self.y / scalar
            return Vector2D(x,y)
        else:
            return None
        
    def __truediv__(self, scalar):
        return self.__div__(scalar)

    def __eq__(self, other):
        if abs(self.x - other.x) < self.thresh:
            if abs(self.y - other.y) < self.thresh:
                return True
        return False

    def __ge__(self, other):
        if self.x >= other.x:
            if self.y >= other.y:
                return True
        return False

    def __lt__(self, other):
        if self.x < other.x: 
            if self.y < other.y: 
                return True
        return False

    def __hash__(self):
        return id(self)

    def __str__(self):
        return "<" + str(self.x) + ", " + str(self.y) + ">"

    def magnitudeSquared(self):
        return self.magnitudeSquared * self.magnitudeSquared

    def magnitude(self):
        return sqrt(self.magnitudeSquared())

    def normalize(self):
        mag = self.magnitude()
        if mag != 0:
            return (self.x/self.magnitude(), self.y/self.magnitude())
        return None
    
    def dot(self, other):
        x = self.x * other.x
        y = self.y * other.y
        return (x+y)

    def copy(self):
        return Vector2D(self.x,self.y)
            
if __name__ == '__main__':
    v1 = Vector2D(2, 3)
    v2 = Vector2D(0.5, -1.5)
    print(f'The sum of {v1} and {v2} is {v1+v2}')
    print(f'The dot product of {v1} and {v2} is {v1.dot(v2)}')