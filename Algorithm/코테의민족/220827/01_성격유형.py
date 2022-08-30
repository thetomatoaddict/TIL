survey=["AN", "CF", "MJ", "RT", "NA"]
choices=[5, 3, 2, 7, 5]
def solution(survey, choices):
    dict1={'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    for i in range(len(survey)):
        if choices[i]<4:
            dict1[survey[i][0]]+=4-choices[i]
        elif choices[i]>4:
            dict1[survey[i][1]]+=choices[i]-4
    answer = ''
    if dict1['T'] > dict1['R']:
        answer+='T'
    else :
        answer+='R'
    if dict1['F'] > dict1['C']:
        answer+='F'
    else :
        answer+='C'
    if dict1['M'] > dict1['J']:
        answer+='M'
    else :
        answer+='J'
    if dict1['N'] > dict1['A']:
        answer+='N'
    else :
        answer+='A'
    return answer

print(solution(survey, choices))