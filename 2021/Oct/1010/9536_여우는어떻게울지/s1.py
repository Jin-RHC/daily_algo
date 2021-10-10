T = int(input())

for tc in range(1, T + 1):
    words = input().split()
    others = {}

    while True:
        target = input()
        if target == 'what does the fox say?':
            break
        else:
            others[target.split()[2]] = 1

    for word in words:
        if others.get(word, 0):
            pass
        else:
            print(word, end=' ')