# 처음 성공한 중복이 많은 코드. 그래도 오히려 좋아~
import sys
sys.stdin = open('input.txt')

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)


def bomb(lst, result, cnt, before, state):
    def transform(visited):
        tt = sorted(list(visited))
        for a, b in tt:
            temp[a].pop(b)
            temp[a].insert(0, 0)
    global answer
    temp_state = 1

    if cnt == N:
        if result >= answer:
            answer = result
        return

    if state:
        temp = [item[:] for item in lst]
        for j in range(H):
            if temp[before][j] != 0:
                temp_state = 0
                if temp[before][j] == 1 and j != H - 1:
                    temp[before][j] = 0
                    bomb(temp, result + 1, cnt + 1, before, 1)

                else:
                    stack = [(before, j)]
                    visited = {(before, j), }
                    while stack:
                        x, y = stack.pop()
                        if temp[x][y] == 1:
                            continue
                        for k in range(4):
                            for m in range(1, temp[x][y]):
                                if 0 <= x + dx[k] * m < W and 0 <= y + dy[k] * m < H:
                                    if temp[x + dx[k] * m][y + dy[k] * m] >= 1 and (x + dx[k] * m, y + dy[k] * m) not in visited:
                                        stack.append((x + dx[k] * m, y + dy[k] * m))
                                        visited.add((x + dx[k] * m, y + dy[k] * m))
                                else:
                                    break
                    transform(visited)
                    bomb(temp, result + len(visited), cnt + 1, before, 0)
                break

    else:
        for i in range(W):
            temp = [item[:] for item in lst]
            for j in range(H):
                if temp[i][j] != 0:
                    temp_state = 0
                    if temp[i][j] == 1 and j != H - 1:
                        temp[i][j] = 0
                        bomb(temp, result + 1, cnt + 1, i, 1)

                    else:
                        stack = [(i, j)]
                        visited = {(i, j), }
                        while stack:
                            x, y = stack.pop()
                            if temp[x][y] == 1:
                                continue
                            for k in range(4):
                                for m in range(1, temp[x][y]):
                                    if 0 <= x + dx[k] * m < W and 0 <= y + dy[k] * m < H:
                                        if temp[x + dx[k] * m][y + dy[k] * m] >= 1 and (x + dx[k] * m, y + dy[k] * m) not in visited:
                                            stack.append((x + dx[k] * m, y + dy[k] * m))
                                            visited.add((x + dx[k] * m, y + dy[k] * m))
                                    else:
                                        break
                        transform(visited)
                        bomb(temp, result + len(visited), cnt + 1, i, 0)
                    break

    if temp_state:
        if result > answer:
            answer = result
        return


T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    bricks = [list(map(int, input().split())) for _ in range(H)]
    bt = [[bricks[j][i] for j in range(H)] for i in range(W)]

    how_many = 0
    for i in bricks:
        for j in i:
            if j > 0:
                how_many += 1
    answer = 0
    bomb(bt[:][:], 0, 0, 0, 0)
    print('#{} {}'.format(tc, how_many - answer))