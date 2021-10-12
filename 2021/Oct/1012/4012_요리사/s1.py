import sys
sys.stdin = open('input.txt')
from itertools import combinations

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    target = N // 2
    comb = combinations(range(N), target)
    answer = 100000000000000
    for i in comb:
        temp_set = set(range(N)) - set(i)
        temp_a = sum([lst[r][c] for r in i for c in i])
        temp_b = sum([lst[r][c] for r in temp_set for c in temp_set])
        if abs(temp_a - temp_b) < answer:
            answer = abs(temp_a - temp_b)

    print('#{} {}'.format(tc, answer))