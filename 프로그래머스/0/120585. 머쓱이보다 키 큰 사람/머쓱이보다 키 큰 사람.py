answer = []
def solution(array, height):
    for i in array:
        if i > height:
            answer.append(i)
    return len(answer)
            



