def f(a, b):
    if a > b or a == 30:
        return 0
    elif a == b:
        return 1
    return f(a + 1, b) + f(a * 2, b) + f(a * 3, b)


print(f(2, 12) * f(12, 36))
# Ответ: 60
