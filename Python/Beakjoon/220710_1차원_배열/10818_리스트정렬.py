n=int(input())
nl=list(map(int,input().split()))
nl.sort() # .sort 메서드는 값을 오름차순으로 정렬함. 
print(nl[0],nl[-1])