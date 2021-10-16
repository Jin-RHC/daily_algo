from collections import deque


def solution(n, results):
    win = [[] for _ in range(n + 1)]
    lose = [[] for _ in range(n + 1)]
    for result in results:
        win[result[0]].append(result[1])
        lose[result[1]].append(result[0])
    answer = 0
    for i in range(1, n + 1):
        visited = [0] * (n + 1)
        dq = deque([i])
        while dq:
            temp = dq.popleft()
            for j in win[temp]:
                if visited[j] == 0:
                    visited[j] = 1
                    dq.append(j)
        dq = deque([i])
        while dq:
            temp = dq.popleft()
            for j in lose[temp]:
                if visited[j] == 0:
                    visited[j] = 1
                    dq.append(j)
        if sum(visited) == n - 1:
            answer += 1

    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))