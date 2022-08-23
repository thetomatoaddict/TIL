def solution(new_id):
    #1단계
    new_id=new_id.lower()
    #2단계
    for i in new_id:
        if i not in 'qwertyuiopasdfghjklzxcvbnm1234567890-_.':
            new_id=new_id.replace(i, '')
    #4단계
    try:
        if new_id[0] == '.' or new_id[-1] == '.':
            while True:
                if new_id[0] == '.' or new_id[-1] == '.':
                    new_id=new_id.rstrip('.')
                    new_id=new_id.lstrip('.')
                else : 
                    break
    except: 
        pass

    #3단계
    dot=''
    for i in new_id:
        if i == '.':
            dot+=i
        elif len(dot)>0 and i != '.':
            new_id=new_id.replace(dot, '.')
            dot=''
    

    #5단계
    if len(new_id) == 0 :
        new_id='a'
    #6단계
    if len(new_id) > 15 :
        new_id=new_id[0:15]
    if new_id[0] == '.' or new_id[-1] == '.':
        while True:
            if new_id[0] == '.' or new_id[-1] == '.':
                new_id=new_id.rstrip('.')
                new_id=new_id.lstrip('.')
            else : break
    #7단계
    if len(new_id) <= 2 :
        while len(new_id) < 3 :
            new_id+=new_id[-1]
    
    answer = new_id
    return answer
userinp='.................ab........................cdefg............hijklmn.p'
a=solution(userinp)
print(a)
# 14 21