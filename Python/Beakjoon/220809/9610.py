n=int(input())
q1=0
q2=0
q3=0
q4=0
axis=0
for _ in range(n):
    n,m=map(int, input().split())
    if n == 0 or m == 0:
        axis+=1
    elif n > 0 :
        if m > 0 :
            q1+=1
        elif m < 0 :
            q4+=1
    elif n < 0 :
        if m < 0 :
            q3+=1
        elif m > 0 :
            q2+=1
print(f'Q1: {q1}\nQ2: {q2}\nQ3: {q3}\nQ4: {q4}\nAXIS: {axis}')