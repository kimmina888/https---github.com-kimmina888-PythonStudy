'''
6
교차점의 개수를 구하는 함수
'''
def solution(left_rings):
    answer = 0
    for i in range(len(left_rings)):
        if left_rings[i] <= i:
            for k in range(0,len(left_rings)-i):
                if i+k > left_rings[i]:
                    answer += 1
    return answer

left = [1,4,2,5,3]
left = [2,4,0,3,1]
print(solution(left))