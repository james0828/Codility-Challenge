def solution(K, M, A):
    # write your code in Python 3.6
    length = len(A)
    acc_map = {}
    result = set()
    for i in range(0, M + 2):
        acc_map[i] = 0
    
    for i in A:
        acc_map[i] += 1

    for index in range(K):
        value = A[index]
        acc_map[value + 1] += 1
        acc_map[value] -= 1
    
    for i in acc_map:
        if acc_map[i] > length / 2:
            result.add(i)
    
    for i in range(0, length - K):
        value1 = A[i]
        value2 = A[i + K]
        
        if value1 == value2:
            continue

        acc_map[value1 + 1] -= 1
        acc_map[value1] += 1
        acc_map[value2 + 1] += 1
        acc_map[value2] -= 1
        
        if acc_map[value] > length / 2:
            result.add(value)
        if acc_map[value2 + 1] > length / 2:
            result.add(value2 + 1)
    
    return sorted(list(result))
