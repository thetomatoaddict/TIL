from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    for i in course :
        tmp=[]
        for j in orders:
            j=sorted(j)
            tmp.extend(list(combinations(j, i)))
        tmp=Counter(tmp).most_common()
        for k,v in tmp:
            if v == list(tmp[0])[1] and v > 1:
                answer.append(''.join(k))
    answer=sorted(answer)
    
    return answer

