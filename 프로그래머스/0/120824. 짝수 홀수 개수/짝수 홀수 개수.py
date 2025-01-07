def solution(num_list):
    result = 0
    result2 = 0
    for i in num_list:
        if i % 2 ==0:
            result +=1
        else:
            result2 +=1
    return [result, result2]

