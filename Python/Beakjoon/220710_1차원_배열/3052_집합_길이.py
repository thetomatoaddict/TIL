n=[]
for i in range(10):
    a=int(input())
    n.append(a%42)
a=set(n) #집합함수
print(len(a)) #길이함수