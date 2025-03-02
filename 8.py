count = 0
letters = 'КОНФЕТА'
for a1 in letters:
    for a2 in letters:
        for a3 in letters:
            for a4 in letters:
                for a5 in letters:
                    a = a1 + a2 + a3 + a4 + a5
                    if a[1] != 'Ф' and a.count('Е') == 2:
                        count += 1

print(count)
# Ответ: 1944
