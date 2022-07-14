word = input()
result = {}
for i in word:
    if i in result:
        result[i] += 1
    else :
        result[i] = 1
for i in result : 
    print(i, result[i]) 


    