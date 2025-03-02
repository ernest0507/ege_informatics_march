file = open('24.txt')
a = file.readline() + '012'
file.close()

tests = ['CACACACA', 'CACACAC', 'ACACACA', 'CACB']
count, countm = 0, 0
x, y = 'CA'
for i in range(len(a) - 3):
    if a[i] == a[i + 2] == x and a[i + 1] == a[i + 3] == y:
        count += 1
        x, y = y, x
    else:
        if count > 0:
            if a[i] + a[i + 1] + a[i + 2] == 'ACA' or a[i] + a[i + 1] + a[i + 2] == 'CAC':
                count += 3
        x, y = 'CA'
        countm = max(countm, count)
        count = 0
print(len('CACACACACACACACACACACACACACACACACACACACACACACACACACACA'))
print(countm)
# Ответ: 54
