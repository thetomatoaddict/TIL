test=int(input())

for i in range(test):
    h,w,n=map(int, input().split())
    if h*w >= n :
        if 9 > n // h > 0 :
            if n % h > 0 :
                print(n%h,'0',n//h+1,sep='')
            elif n % h == 0 :
                print(h,'0',n//h,sep='')
        elif 9 <= n // h :
            if n % h > 0 :
                print(n%h,n//h+1,sep='')
            elif n % h == 0 :
                print(h,n//h,sep='')    
        elif n // h == 0 :
            print(n,0,1,sep='')  
