def solution(mho_cards, mhe_cards):
    ans = [0 for i in range(2)]
    result = -1
    for i in len(mho_cards):
        if(mho_cards[i] > mhe_cards[i]):
            ans[0]+=1
        elif(mho_cards[i] < mhe_cards[i]):
             ans[1]+=1
    if(ans[0]>ans[1]): result = 1
    elif(ans[0]<ans[1]): result = 0
    return result
