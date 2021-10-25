from collections import defaultdict


def solution(genres, plays):
    length = len(plays)
    musics = defaultdict(list)
    playtimes = {}
    answer = []
    for i in range(length):
        musics[genres[i]].append((plays[i], -i))
        playtimes[genres[i]] = playtimes.get(genres[i], 0) + plays[i]
    new_genres = sorted(list(playtimes.items()), key=lambda x: x[1], reverse=True)
    for key in musics.keys():
        musics[key].sort()
    for genre, _ in new_genres:
        cnt = 0
        while cnt < 2 and musics[genre]:
            answer.append(- musics[genre].pop()[1])
            cnt += 1
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))