dwarfs=[int(input()) for _ in range(9)]

tmp=set()
for i in range(9):
    if len(tmp) == 2 :
        break
    for j in range(i-1, 9):
        if dwarfs[i] != dwarfs[j] :
            if sum(dwarfs) - (dwarfs[i]+dwarfs[j]) == 100 :
                tmp.add(dwarfs[i])
                tmp.add(dwarfs[j])
                break
dwarfs=sorted(list(set(dwarfs)-tmp))
print(*dwarfs,sep='\n')
