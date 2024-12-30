def solution(sides):
    m = max(sides)
    sides.remove(max(sides))
    sum= 0
    for i in sides:
        sum += i
    if sum > m:
        return 1
    else: 
        return 2