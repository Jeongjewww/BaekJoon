N = int(input())
P = list(map(int, input().split()))
sum = 0
P.sort()
for i in range(N):
    sum += P[i] * (N-i)
print(sum)