from collections import deque


def solution(n, edge):
    visited = [0] * (n + 1)
    visited[1] = 1
    lst = [[] for _ in range(n + 1)]
    for i in edge:
        lst[i[0]].append(i[1])
        lst[i[1]].append(i[0])
    dq = deque([1])
    while dq:
        curr = dq.popleft()
        for i in lst[curr]:
            if visited[i] == 0:
                visited[i] = visited[curr] + 1
                dq.append(i)

    maximum = max(visited)
    answer = 0
    for i in visited:
        if i == maximum:
            answer += 1

    return answer