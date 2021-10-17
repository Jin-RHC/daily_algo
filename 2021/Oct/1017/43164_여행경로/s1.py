def solution(tickets):
    def search(lst, cnt):
        if len(set(lst)) == len(cities) and cnt == N:
            answer.append(lst)
        for idx, value in enumerate(d_a.get(lst[-1], [])):
            if visited[lst[-1]][idx] == 0:
                state = 0
                visited[lst[-1]][idx] = 1
                search(lst + [value], cnt + 1)
                visited[lst[-1]][idx] = 0
    d_a = {}
    visited = {}
    cities = set()
    N = len(tickets)
    for a, b in tickets:
        d_a[a] = d_a.get(a, []) + [b]
        cities.add(a)
        cities.add(b)
    for key in d_a.keys():
        d_a[key].sort()
        visited[key] = [0] * len(d_a[key])
    answer = []
    search(['ICN'], 0)
    return answer[0]