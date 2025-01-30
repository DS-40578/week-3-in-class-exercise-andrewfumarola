x = lambda a: a+1
print(x(5))

slope = lambda x1, y1, x2, y2: (x2 - x1) / (y2 - y1)
print(slope(0, 4, 3, 3))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

