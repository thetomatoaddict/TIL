tc = int(input())

for i in range(tc):
    current_range=0
    current_speed=0
    sec=int(input())
    for j in range(sec):
        ctrl = list(map(int, input().split()))
        if ctrl[0] == 0 :
            current_range+=current_speed
        if ctrl[0] == 1 :
            current_speed+=ctrl[1]
            current_range+=current_speed

        if ctrl[0] == 2 :
            current_speed-=ctrl[1]
            if current_speed < 0 :
                current_speed=0
            current_range+=current_speed
    print(f'#{i+1} {current_range}')
