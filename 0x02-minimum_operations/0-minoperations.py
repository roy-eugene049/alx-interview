import sys

def minOperations(n):
    dp = [sys.maxsize] * (n+1)
    dp[1] = 0
    
    for i in range(2, n+1):
        for j in range(1, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + (i//j - 1))
    
    return dp[n] if dp[n] != sys.maxsize else 0
