class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "<Point {}, {}>".format(self.x, self.y)

    def distance(self, other):
        """
        :type other: Point
        :rtype int
        """
        return abs(self.x - other.x) + abs(self.y - other.y)


shop_positions = [
    Point(1, 1),
    Point(2, 5),
    Point(5, 4)
]

for i in range(len(shop_positions)):
    for j in range(i + 1, len(shop_positions)):
        distance = shop_positions[i].distance(shop_positions[j])
        print('{} -> {} の距離'.format(i, j), distance)
