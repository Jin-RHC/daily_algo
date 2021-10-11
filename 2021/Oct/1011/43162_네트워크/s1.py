def solution(n, computers):
    visited = [0] * n
    for i in range(n):
        computers[i][i] = 0
    lst = []
    answer = 0
    for i in range(n):
        if visited[i] == 0:
            for j in range(n):
                if computers[i][j]:
                    lst.append(j)
                while lst:
                    temp = lst.pop()
                    visited[temp] = 1
                    for k in range(n):
                        if computers[temp][k] and visited[k] == 0:
                            lst.append(k)
            answer += 1

    return answerdef solution(n, computers):
    visited = [0] * n
    for i in range(n):
        computers[i][i] = 0
    lst = []
    answer = 0
    for i in range(n):
        if visited[i] == 0:
            for j in range(n):
                if computers[i][j]:
                    lst.append(j)
                while lst:
                    temp = lst.pop()
                    visited[temp] = 1
                    for k in range(n):
                        if computers[temp][k] and visited[k] == 0:
                            lst.append(k)
            answer += 1

    return answer