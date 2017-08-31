def bersuball():
    n = int(input())
    boys = sorted([int(skill) for skill in input().split(' ')])
    m = int(input())
    girls = sorted([int(skill) for skill in input().split(' ')])

    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1, m+1):
      for j in range(1, n+1):
        take = abs(boys[j-1] - girls[i-1]) <= 1
        if take:
          dp[i][j] = dp[i-1][j-1] + 1
        dp[i][j] = max(dp[i][j], dp[i-1][j], dp[i][j-1])

    return dp[m][n]
print(bersuball())    
