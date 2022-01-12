def func_a(arr):
    total = 0
    for i in arr:
        total += i
    return total

def solution(total, arr):
    result = []
    req_total : func_a(arr)
    for i in arr :
        if req_total > total:
            result.append(arr)
        else:
            result.append(total/len(arr))
    return result
