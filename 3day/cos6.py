def solution(string):
    answer = 0
    number = 0
    s = string+''
    for c in s:
        if c >= '0' and c <='9':
            number = number + int(c)
        else:
            answer += number
            number = 0
    return answer