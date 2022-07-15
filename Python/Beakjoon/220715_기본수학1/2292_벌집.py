n=int(input())
step=1
six=6
while n>1:
    n-=six
    step+=1
    six+=6

print(step)