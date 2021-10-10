from collections import deque
N = int(input())
lst = list(map(int, input().strip().split()))
stack = deque([])
idx = N - 1

while idx > 0:
    stack.append(idx)
    if lst[idx] <= lst[idx - 1]:
        while stack and lst[stack[-1]] <= lst[idx - 1]:
            lst[stack.pop()] = str(idx)
    idx -= 1

while stack:
    lst[stack.pop()] = '0'
lst[0] = '0'
print(' '.join(lst))