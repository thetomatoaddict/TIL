
def count_a(a):
    a=list(a)
    count=0
    for i in range(len(a)):
        if a.pop()=='a':
            count+=1
    return count
a=input()
print(count_a(a))
