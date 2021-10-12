import sys
sys.stdin = open('input.txt')

dx = (-1, 1, 1, -1)
dy = (1, 1, -1, -1)


def des(r, c, visited, ne, se):
    """
    북동-남동-남서-북서 순서로 탐색을 한다.
    북동과 남동으로 얼마나 갔는지만 알면 나머지는 자동으로 나오므로 변수 생략
    :param r: 기준점의 행 좌표
    :param c: 기준점의 열 좌표
    :param visited: 어디 갔는지 저장하는 set
    :param ne: 북동쪽으로 얼마나 갔는지 저장
    :param se: 남동쪽으로 얼마나 갔는지 저장
    :return: None
    """
    global answer
    if se != 0:
        for a in range(1, ne + 1):
            if 0 <= r + dx[2] * a < N and 0 <= c + dy[2] * a < N:
                if lst[r + dx[2] * a][c + dy[2] * a] not in visited:
                    visited.add(lst[r + dx[2] * a][c + dy[2] * a])
                else:
                    return
            else:
                return
        stx, sty = r + dx[2] * ne, c + dy[2] * ne  # 마지막 방향으로의 탐색 시 기준접
        for b in range(1, se):
            if 0 <= stx + dx[3] * b < N and 0 <= sty + dy[3] * b < N:
                if lst[stx + dx[3] * b][sty + dy[3] * b] not in visited:
                    visited.add(lst[stx + dx[3] * b][sty + dy[3] * b])
                else:
                    return
            else:
                return
        if len(visited) > answer:
            answer = len(visited)

    elif ne != 0:
        temp = 1
        while r + temp * dx[1] < N - ne + 1 and c + temp * dy[1] < N:
            if lst[r + temp * dx[1]][c + temp * dy[1]] not in visited:
                visited.add(lst[r + temp * dx[1]][c + temp * dy[1]])
                des(r + temp * dx[1], c + temp * dy[1], visited.copy(), ne, temp)
            else:
                return
            temp += 1

    else:
        temp = 1
        while temp <= r and c + temp < N - 1:
            if lst[r - temp][c + temp] not in visited:
                visited.add(lst[r - temp][c + temp])
                des(r - temp, c + temp, visited.copy(), temp, se)  # copy()를 꼭 써줘야 함.
            else:
                break
            temp += 1


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    answer = -1
    for i in range(1, N - 1):
        for j in range(N - 2):
            des(i, j, {lst[i][j], }, 0, 0)

    print('#{} {}'.format(tc, answer))

