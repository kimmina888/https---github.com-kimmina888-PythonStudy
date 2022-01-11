'''
5
369게임을 하기 위해 숫자를 주면 박수를 몇번치는지 알아내느 함수
전달되는 number는 2자리 이상의 정수
'''
def solution(number):
    count = 0
    for i in range(number,number+1):
        current = i
        while current != 0:
            unit = current % 10
            if unit == 3 or unit == 6 or unit == 9:
                count += 1
            current /= 10
    return current

print(solution(33))