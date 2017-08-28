shop_positions = [
    [1, 1],
    [2, 5],
    [5, 4]
]

for i in range(len(shop_positions)):
    for j in range(i + 1, len(shop_positions)):
        distance = abs(shop_positions[i][0] - shop_positions[j][0]) + abs(shop_positions[i][1] - shop_positions[j][1])
        print('{} -> {} の距離'.format(i, j), distance)
