def F(x, y, z, w):
    return int((x or not (y)) and not (x == z) and w)


print('x y z w | F')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if F(x, y, z, w):
                    print(x, y, z, w, '|', F(x, y, z, w))
# Ответ: zyxw
