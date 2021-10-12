# 중복을 약간 줄였으나 사실 전 것보다 크게 좋아진 건 못 느끼겠다.
import sys
sys.stdin = open('input.txt')

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)


def bomb(lst, result, cnt, before, state):
    def transform(visited): # 폭발하고 난 이후의 리스트를 정렬시킴
        tt = sorted(list(visited))
        for a, b in tt:
            temp[a].pop(b)
            temp[a].insert(0, 0)
    global answer
    temp_state = 1 # 모두 다 0이 되었을 때를 고려해주기 위함

    if cnt == N:
        if result > answer:
            answer = result
        return

    # 전에 굳이 1을 뽑았다면 이번에도 해당 열을 뽑아줘야 함.
    target = [before] if state else range(W)

    for i in target:
        temp = [item[:] for item in lst]
        for j in range(H):
            if temp[i][j] == 1 and j != H - 1:
                temp_state = 0
                temp[i][j] = 0
                bomb(temp, result + 1, cnt + 1, i, 1)
                break

            elif temp[i][j] != 0:
                temp_state = 0
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
    bt = [[bricks[j][i] for j in range(H)] for i in range(W)] # 귀찮아서 트랜스포즈해줌

    how_many = 0
    for i in bricks:
        for j in i:
            if j > 0:
                how_many += 1
    answer = 0
    bomb(bt[:][:], 0, 0, 0, 0)
    print('#{} {}'.format(tc, how_many - answer))