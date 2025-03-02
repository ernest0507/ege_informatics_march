file = open('9.txt')

count = 0
for line in file:
    line = line.replace('\n', '').replace('\t', ' ').split(' ')
    line = list(map(int, line))
    if len(set(line)) == len(line) and (max(line) + min(line)) < (sum(line) - max(line) - min(line)):
        count += 1

print(count)
# Ответ: 2842
