#--1. 배열 b 내림차순으로 정렬하는 방법
# n = int(input())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))

# a.sort()
# b.sort(reverse=True)
# result = 0
# for i in range(n):
#     result += a[i]*b[i]
# print(result)

#--2. b의 최댓값을 곱하고 해당 배열에서 제거하는 방법
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
result = 0
for i in range(n):
    result += a[i]*max(b)
    b.remove(max(b))
print(result)