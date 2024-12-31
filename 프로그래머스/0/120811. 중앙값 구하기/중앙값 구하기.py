def solution(array):
    array = sorted(array)
    if len(array) <= 3:
        return array[len(array)//2]
    elif len(array) >3:
        return array[len(array)//2]  
   