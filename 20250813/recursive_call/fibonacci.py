def fibonacci(n):
    return n if n < 2 else fibonacci(n - 1) + fibonacci(n - 2)

m = 6
def fibonacci_memoization(n):
    
    if n >= 2 and memo[n] == 0 :
        memo[n] =  fibonacci_memoization(n-1) +  fibonacci_memoization(n-2)
    return memo[n]
memo = [0] * (m + 1)
memo[1] = 1

print(fibonacci_memoization(6))

def fibonacci_DP(n):
    f = [0] * (n + 1)
    f[1] = 1
    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]
