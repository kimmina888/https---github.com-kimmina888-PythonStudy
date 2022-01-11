'''
9
중복되는 문자 제거
"senteeeencccccceeeee"라는 문장이 주어진다면 "sentence"라는 결과물이 나오게 
소문자 알파벳 characters 변수
한줄만 변경
'''
def solution(characters):
    result = [characters[0]]
    for i in range(1, len(characters)):
        if characters[i-1] != characters[i]:
            result.append(characters[i])
    return ''.join(result)
print(solution('senteeeencccccceeeee'))