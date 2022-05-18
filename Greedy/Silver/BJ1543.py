#--Silver4 문서 검색--#

doc = input()
sch = input()
cnt = 0; i = 0

while i <= len(doc)-len(sch):
    if doc[i:i+len(sch)] == sch:
        cnt += 1
        i += len(sch)
    else: i += 1
print(cnt)