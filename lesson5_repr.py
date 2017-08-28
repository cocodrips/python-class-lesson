class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        '''printした時に何を表示するかを宣言できる'''
        return "<Point {}, {}>".format(self.x, self.y)


shop_positions = [
    Point(1, 1),
    Point(2, 5),
    Point(5, 4)
]

print(shop_positions)
