def solution(triangle):
    length = len(triangle)
    lst = [[0] * i for i in range(1, length + 1)]
    for i in range(length):
        for j in range(i + 1):
            if j == 0:
                lst[i][j] = lst[i - 1][0] + triangle[i][j]
            elif i == j:
                lst[i][j] = lst[i - 1][i - 1] + triangle[i][j]
            else:
                lst[i][j] = max(lst[i - 1][j - 1], lst[i - 1][j]) + triangle[i][j]
    answer = max(lst[length - 1])
    return answer