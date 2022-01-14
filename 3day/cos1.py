import math
def solution(a, b):
    answer = 0 
    diff = a- b if a > b else b- a
    answer = 10 / diff
    return answer * 60
print(solution(10, 5))
print(solution(5 ,10))
print(solution(10, 8))
print(solution(8 ,10))