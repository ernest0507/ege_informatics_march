for x in range(10):
    a = int(f'{x}B09', 17)
    b = int(f'{x}8E8', 15)
    if (a + b) % 155 == 0:
        print((a + b) // 155)
# Ответ: 194
