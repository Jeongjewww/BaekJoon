def salt(N):
    if N%5==0: return N//5
    else:
        x = N//5
        while (x>=0):
            r = N - 5 * x
            if r == 0: return -1
            elif r%3 == 0: return x+r//3
            else:
                x -= 1
        return -1
            
N = int(input())
print(salt(N))