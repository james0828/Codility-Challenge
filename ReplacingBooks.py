def solution(A, K):
    acc_num = {}
    result = 0
    length = len(A)
    last = 0

    for index, value in enumerate(A):
        if value in acc_num:
            acc_num[value] += 1
        else:
            acc_num[value] = 1
        
        if acc_num[value] > result:
            result = acc_num[value]
        else:
            if index - last - result + 1 > K:
                acc_num[A[last]] -= 1
                last += 1
    
    return min(result + K, length)
