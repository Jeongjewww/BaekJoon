n = int(input())
change = [500, 100, 50, 10, 5, 1]
cnt = 0; x = 0
rest = 1000 - n
for i in change:
    x = rest // i
    cnt += x
    rest -= x*i
print(cnt)