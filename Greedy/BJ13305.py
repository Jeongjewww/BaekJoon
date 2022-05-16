num = int(input())
dis = list(map(int, input().split()))
price = list(map(int, input().split()))

min = price[0]
total = dis[0]*price[0]
for i in range(1, num-1):
    if price[i] < min:
        min = price[i]
    total += min*dis[i]
print(total)