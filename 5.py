def f(N):
    num = bin(N)[2:]
    num = num + num[-2]
    num = num + num[1]
    return int(num, 2)


for N in range(2, 100):
    R = f(N)
    if R > 150:
        print(N)
# Ответ: 38
