# Pointクラスを作る 
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Pointクラスでお店の座標を表現
shop_positions = [
    Point(1, 1),
    Point(2, 5),
    Point(5, 4)
]


# 配列ではなくPointで受け取るようにする
def get_dictance(p0, p1):
    return abs(p0.x - p1.x) + abs(p0.y - p1.y)


for i in range(len(shop_positions)):
    for j in range(i + 1, len(shop_positions)):
        distance = get_dictance(shop_positions[i], shop_positions[j])
        print('{} -> {} の距離'.format(i, j), distance)
