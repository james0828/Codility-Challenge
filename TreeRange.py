import sys
sys.setrecursionlimit(10000000)

def solution(T):
    # write your code in Python 3.6
    length = len(T)
    adj_list = [[] for _ in range(0, length)]
    dp = [[(0, 0) for _ in range(0, length)] for _ in range(0, length - 1)]
    count = 0

    for i, j in enumerate(T):
        adj_list[i].append(j)
        adj_list[j].append(i)
    
    def find_route(start, end, current_node, min_node, max_node):
        for elem in adj_list[current_node]:
            if elem == end:
                dp[start][end] = (min_node, max_node)
                break
            elif check_list[elem]:
                tmp_min = min(elem, min_node)
                tmp_max = max(elem, max_node)
                check_list[elem] = False
                find_route(start, end, elem, tmp_min, tmp_max)
    
    for i in range(0, length - 1):
        check_list = [True for _ in range(0, length)]
        check_list[i] = False
        find_route(i, i + 1, i, i, i + 1)
    
    for i in range(0, length - 2):
        for j in range(i + 2, length):
            dp[i][j] = min(dp[i][j - 1][0], dp[j - 1][j][0]), max(dp[i][j - 1][1], dp[j - 1][j][1])
    
    for i in range(0, length):
        for j in range(0, length):
            if i == j or ( i < j and i == dp[i][j][0] and j == dp[i][j][1]):
                count += 1
    
    return count
