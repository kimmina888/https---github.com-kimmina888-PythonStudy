'''
3
모의고사 성적이 들어있는 리스트 scores
200점 이하의 점수 세기
#한줄 수정하기
'''
def solution(scores):
    count=0
    for s in range(0, len(scores)): #그냥 scores를 넣으면 값을 가져온다. 인덱스를 가져오고 싶다면 len()을 사용하여야 한다.
        if scores[s] <= 200:
            count += 1
    return count

scores = [200,300]
print(solution(scores))

# def solution(scores):
#     count=0
#     for s in range(scores):
#         if scores[s] <= 200:
#             count += 1
#     return count
