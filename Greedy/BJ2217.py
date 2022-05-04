# 입력받은 값을 내림차순으로 정렬, n번째 값에 n을 곱한 값들 중 최댓값 출력
n = int(input())
x = []; k = []
for i in range(n):
    x.append(int(input()))
x.sort(reverse = True)
for i in range(n):
    k.append(x[i]*(i+1))
print(max(k))