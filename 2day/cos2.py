'''
2
학생들 신발 사이즈 조사
축구화 사이즈 작은 순서대로 "7", "7.5", "8", "8.5", "9", "9.5" 총 6종류
원하는 사이즈 리스트 shoes_size
가장 작은 사이즈부터 순서대로 리스트에 담아 return
'''
def solution(shoes_size):
    answer = [0 for _ in range(len(shoes_size))]
    for i in shoes_size.sort():
        answer.append(i)
    return answer

shoes = [9,8,8.5,7,7.5,9,9.5]
shoes = solution(shoes)
for s in shoes:
    print(s)