def solution(arr):
    answer = [arr[0]]
    #현재 인덱스 앞 또는 뒤에 값과 비교
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
            
    return answer