cal = input().split('-')
_cal = []
result = 0
for value in cal:
    sum = 0
    if '+' not in value:
        _cal.append(int(value))
    elif '+' in value:
        _value = value.split('+')
        for i in range(len(_value)):
            sum += int(_value[i])
        _cal.append(sum)
result += _cal[0]
for i in _cal[1:]:
    result -= i
print(result)