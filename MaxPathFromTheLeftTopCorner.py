def solution(A):
    width = len(A)
    height = len(A[0])
    dp = [[0 for _ in range(0, height)] for _ in range(0, width)]
    for i in range(0, width):
        for j in range(0, height):
            if i == 0 and j == 0:
                dp[i][j] = A[i][j]
            elif i == 0:
                dp[i][j] = dp[i][j - 1] * 10 + A[i][j]
            elif j == 0:
                dp[i][j] = dp[i - 1][j] * 10 + A[i][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) * 10 + A[i][j]

    return str(dp[width - 1][height - 1])
