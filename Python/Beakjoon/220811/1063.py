import sys
sys.stdin = open("1063.txt")
delta=[[1,0],[-1,0],[0,-1],[0,1]]


king,stone,n=map(str, input().split())
king=[ord(king[0]),int(king[1])]
stone=[ord(stone[0]),int(stone[1])]
move=''
moveint=[]
for _ in range(int(n)):
    move=input()
    if king[0] >= 65 and stone[0]>=65 and stone[1]>0 and king[1]>0:
        if move[0] == 'R' :
            king[0]+=delta[0][0]
            stone[0]+=delta[0][0]
        elif move[0] == 'L' :
            king[0]+=delta[1][0]
            stone[0]+=delta[1][0]
        elif move[0] == 'B' :
            king[1]+=delta[2][1]
            stone[1]+=delta[2][1]
        elif move[0] == 'T' :
            king[1]+=delta[3][1]
            stone[1]+=delta[3][1]

        if len(move) == 2 :
            if move[0] == 'R' :
                king[0]+=delta[0][0]
                stone[0]+=delta[0][0]
            elif move[0] == 'L' :
                king[0]+=delta[1][0]
                stone[0]+=delta[1][0]
            elif move[0] == 'B' :
                king[1]+=delta[2][1]
                stone[1]+=delta[2][1]
            elif move[0] == 'T' :
                king[1]+=delta[3][1]
                stone[1]+=delta[3][1]
    result=[king[0],king[1],stone[0],stone[1]]
    
if king[0] < 65 or stone[0]<65 or stone[1]>=0 or king[1]>=0:
    print(f'{chr(result[0])}{result[1]}\n{chr(result[2])}{result[3]}')
else:
    print(f'{chr(king[0])}{king[1]}\n{chr(stone[0])}{stone[1]}')