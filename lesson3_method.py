shop_positions = [
    [1, 1],
    [2, 5],
    [5, 4]
]

# 距離の計算に名前をつけて、部品(関数)化してあげる
def get_dictance(p0, p1):
    return abs(p0[0] - p1[0]) + abs(p0[1] - p1[1])


for i in range(len(shop_positions)):
    for j in range(i + 1, len(shop_positions)):
        distance = get_dictance(shop_positions[i], shop_positions[j])
        print('{} -> {} の距離'.format(i, j), distance)
