class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "<Point {}, {}>".format(self.x, self.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    @staticmethod
    def distance(p1, p2):
        """
        :type p1: Point
        :type p2: Point
        :rtype int
        """
        diff = p1 - p2
        return abs(diff.x) + abs(diff.y)


shop_positions = [
    Point(1, 1),
    Point(2, 5),
    Point(5, 4)
]

print(shop_positions[0] - shop_positions[1])
for i in range(len(shop_positions)):
    for j in range(i + 1, len(shop_positions)):
        distance = Point.distance(shop_positions[i], shop_positions[j])
        print('{} -> {} の距離'.format(i, j), distance)
