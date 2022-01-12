from typing import AnyStr


def solution(table):
    result = [0 for i in range(len(table))]
    for i in range(1, len(table)):
        for j in len(table[i]):
            if(table[0][j] ==table[i][j]):
                answer[i-1] += 1
    answer = 0
    for i in range(len(result)):
        if result[i] > result[answer]:
            answer = i
    return answer