'''
4
국가신용등급에따라 관세
등급        관세율
"S"         5%
"G"         10%
"V"         15%
예: "S"인 국가에서 수입하는 물품의 가격이 1000원인 경우 관세율 5% 적용한 가격은 1050원
'''
def solution(price, grade):
    answer = 0
    if grade == 'S':
        answer = price + (price * 5 / 100)
    elif grade == 'G':
        answer =  price + (price * 10 / 100)
    elif grade == 'V':
        answer =  price + (price * 15 / 100)

    return answer

print(solution(1000,'S'))
