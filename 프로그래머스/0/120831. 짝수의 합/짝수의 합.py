def solution(n):
    answer = 0
    for n in range (0, n+1, 2):
        answer += n
    return answer