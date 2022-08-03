words=[input() for _ in range(5)]

for i in range(15):
    for j in words:
        try:
            print(j[i],end='')
        except:
            continue
