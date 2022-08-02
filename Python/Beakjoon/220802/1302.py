# import sys
from collections import Counter
# input = sys.stdin.readline
N = int(input())
books=[]
result=[]
for _ in range(N) :
    books.append(input())
books=Counter(books).most_common()
for k,v in books:
    if books[0][1] == v:
        result.append(k)
result = sorted(result)

print(result[0])
