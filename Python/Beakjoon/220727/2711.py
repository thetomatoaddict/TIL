tc=int(input())
for i in range(tc):
    word=list(map(str,input().split()))
    where=int(word[0])
    print(word[1][0:where-1],word[1][where:],sep='')