import sys
txt = sys.stdin.read().replace(' ', '').replace('\n', '')
maxcnt=0
result=set()
for i in txt:
    if txt.count(i) > maxcnt :
        maxcnt = txt.count(i)
for i in txt:
    if txt.count(i) == maxcnt :
        result.add(i)
result=list(sorted(result))
print(*result,sep='')