num = int(input())
dp = [i for i in range(num + 1)]
for i in range(2, num + 1):
    for j in range(1, int(i ** (0.5)) + 1):
        dp[i] = min(dp[i], dp[i - j * j] + 1)
print(dp[-1])