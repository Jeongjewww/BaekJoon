t = int(input())

def result(t):
    min = t//60
    sec = t%60
    a = min//5; b = min%5
    if sec%10 != 0: 
        print(-1)
    else: 
        c = sec//10
        print(a, b, c)
result(t)