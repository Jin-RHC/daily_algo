from collections import deque

def solution(begin, target, words):
    length = len(words[0])
    visited = {}
    for i in words:
        visited[i] = 0

    engine = {}
    for word in words:
        for j in range(length):
            engine[word[:j] + '0' + word[j + 1:length]] = engine.get(word[:j] +
                                                                     '0' + word[j + 1:length], []) + [word]
    dq = deque([])
    for i in range(length):
        for j in engine.get(begin[:i] + '0' + begin[i + 1:length], []):
            visited[j] = 1
            dq.append((j, 1))
    while dq:
        word, cnt = dq.popleft()
        if word == target:
            return cnt

        for i in range(length):
            for j in engine.get(word[:i] + '0' + word[i + 1:length], []):
                if visited[j] == 0:
                    visited[j] = 1
                    dq.append((j, cnt + 1))

    return 0