
def sum_List(scores):
    sum = 0
    for score in scores:
        sum += score
    return sum

scores = {10,3,20,50}
print(sum_List(scores))
