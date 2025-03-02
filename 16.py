def F(n):
    if n >= 1000:
        return 1000
    elif n < 1000 and n % 2 != 0:
        return n * F(n + 1)
    elif n < 1000 and n % 2 == 0:
        return (n * F(n + 1)) / 2


print(F(998) / F(1001))

dp = [0] * (1001 + 1)
for n in range(len(dp) - 1, 0, -1):
    if n >= 1000:
        dp[n] = 1000
    elif n < 1000 and n % 2 != 0:
        dp[n] = n * dp[n + 1]
    elif n < 1000 and n % 2 == 0:
        dp[n] = (n * dp[n + 1]) / 2

print(dp[998] / dp[1001])
# Ответ: 498501
