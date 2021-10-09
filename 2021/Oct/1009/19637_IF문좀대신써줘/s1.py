import sys

def bin_search(number):
    start = 1
    end = N
    while start <= end:
        mid = (start + end) // 2
        if benchmarks[mid - 1] < number <= benchmarks[mid]:
            return titles[mid]
        elif number <= benchmarks[mid]:
            end = mid - 1
        else:
            start = mid + 1

N, M = map(int, input().split())
benchmarks = [-1] * (N + 2)
titles = ['none'] * (N + 2)
for i in range(N):
    title, benchmark = sys.stdin.readline().split()
    titles[i + 1] = title
    benchmarks[i + 1] = int(benchmark)
benchmarks[N + 1] = 1000000007
titles[N + 1] = 'none'
for j in range(M):
    print(bin_search(int(sys.stdin.readline())))