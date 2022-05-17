#--Silver 1 A→B--#

n, N = input().split()
n = int(n); N = int(N)
result = 1

while True:
    if n == N:
        print(result)
        break
    elif n > N:
        print(-1)
        break
    else:
        if N%10 == 1:
            N //= 10
        elif N%2 == 0:
            N //= 2
        elif N%2 != 1:
            print(-1)
            break
        result += 1