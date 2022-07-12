a, b = map(int,input().split())
c = (a if (a>=b) else b) # Assign a if a>=b, else assign b
print(int(c))
