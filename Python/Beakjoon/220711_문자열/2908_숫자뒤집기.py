a,b=map(str, input().split())
a=list(a)
b=list(b)
a.reverse()
b.reverse()
ra=(int(a[0])*100)+(int(a[1])*10)+(int(a[2]))
rb=(int(b[0])*100)+(int(b[1])*10)+(int(b[2]))

print(ra if ra>rb else rb)