answers=[1,3,2,4,2,2,4,5]
def solution(answers):
    s1=[1, 2, 3, 4, 5]
    s2=[2, 1, 2, 3, 2, 4, 2, 5]
    s3=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score={1:0,2:0,3:0}
    answer = []
    for i in range(len(answers)):
        s1.append(s1[i])
        if answers[i] == s1[i]:
            score[1]+=1
    for i in range(len(answers)):
        s2.append(s2[i])
        if answers[i] == s2[i]:
            score[2]+=1
    for i in range(len(answers)):
        s3.append(s3[i])
        if answers[i] == s3[i]:
            score[3]+=1
    score=sorted(score.items(),key=lambda x:x[1],reverse=True)
    answer.append(score[0][0])
    if score[0][1] == score[1][1]:
        answer.append(score[1][0])
    if score[0][1] == score[2][1]:
        answer.append(score[2][0])

    return answer
print(solution(answers))