file = open('17.txt')
nums = [int(x) for x in file]
file.close()
maxelem = max(x for x in nums if 10 <= x <= 99)

ans = []
for i in range(len(nums) - 1):
    a, b = nums[i], nums[i + 1]
    check = [100 <= x <= 999 for x in (a, b)]
    if check.count(True) >= 1 and (a + b) % maxelem == 0:
        ans.append(a + b)

print(len(ans), max(ans))
# Ответ: 11 3430
