import sys

n = int(input())
for i in range(n):
    score = []
    m = int(input())
    for i in range(m):
        first, sec = map(int, sys.stdin.readline().split())
        score.append([first, sec])
    score.sort()

    cnt = 1
    max = score[0][1]
    for i in range(1, m):
        if max > score[i][1]:
            cnt += 1
            max = score[i][1]
    print(cnt)