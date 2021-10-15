import sys
sys.stdin = open('input1.txt')

lst = [0] * 2020001
N = int(sys.stdin.readline().rstrip())

answer = 'YES'
for i in range(N):
    x, r = map(int, sys.stdin.readline().rstrip().split())
    if lst[x - r + 1010000] or lst[x + r + 1010000]:
        answer = 'NO'
        break
    elif sum(lst[x - r + 1010000:x + r + 1010000 + 1]) % 3:
        answer = 'NO'
        break
    lst[x - r + 1010000] = 1
    lst[x + r + 1010000] = 2

print(answer)


