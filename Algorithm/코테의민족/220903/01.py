id_list=["con", "ryan"]
report=	["ryan con", "ryan con", "ryan con", "ryan con"]
k=3
def solution(id_list, report, k):
    dict1={}
    dict2={}
    answer=[]
    report=list(set(report))

    #신고당한 유저
    for i in id_list: 
        dict1[i]=[]
        dict2[i]=[]
    for j in report:
        dict1[list(j.split())[1]].append(1)
    for i,j in dict1.items():
        if sum(j) < k :
            dict1[i]=[0]
        elif sum(j) >= k :
            dict1[i]=[1]
    
    # 신고 한 사람
    for i in report:
        if sum(dict1[list(i.split())[1]]) == 1:
            dict2[list(i.split())[0]].append(1)

    for i,j in dict2.items():
        answer.append(sum(j))
            
    return answer

print(solution(id_list, report, k))

    
    
 