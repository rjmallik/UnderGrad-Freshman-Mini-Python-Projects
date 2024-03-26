import math
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'({self.x},{self.y})'
    def distance(self, point):
        return math.sqrt(((self.x-point.x)**2)+((self.y-point.y)**2))
    def __add__(self, point):
        return Point2D((self.x+point.x), (self.y+point.y))
    def __sub__(self, point):
        return Point2D((self.x-point.x), (self.y-point.y))
    def __mul__(self, scalar):
        return Point2D((self.x*scalar), (self.y*scalar))
    def __eq__(self, point):
        if self.x==point.x and self.y==point.y:
            return True
        if Point2D.distance(self, point) <= 0.000001:
            return True
        return False

if __name__ == '__main__':
    A = Point2D(1, 1)
    B = Point2D(0, 0)
    C = Point2D(0, 3)
    D = Point2D(0, 1)
    print(A)             # should print (1.0, 1.0)
    assert A == Point2D(1,1)
    print(A + B)         # should print (1.0, 1.0)
    assert A + B == Point2D(1,1)
    print(A - C)         # should print (1.0, -2.0)
    assert A - C == Point2D(1, -2)
    print(A * 3)         # should print (3.0, 3.0)
    assert A * 3 == Point2D(3, 3)
    print(D.distance(C)) # should print 2.0
    assert D.distance(C) == 2.0
    print(B == A)        # should print False
    assert B != A
    print(B == A * 0)    # should print True
    assert B == A * 0
    print('Everything works correctly!')

