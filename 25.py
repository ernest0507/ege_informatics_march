def dividers(n):
    div = set()
    for d in range(1, int(n ** 0.5) + 1):
        if n % d == 0:
            div.add(d)
            div.add(n // d)
    return div


count = 0
num = 700_000 + 1
while count < 5:
    divs = []
    for x in dividers(num):
        if x % 10 == 7 and x != num and x != 7:
            divs.append(x)
    if len(divs) > 0:
        print(num, min(divs))
        count += 1
    num += 1
# Ответ:
# 700002 27
# 700003 37
# 700005 6087
# 700007 77
# 700008 29167
