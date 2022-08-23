from collections import Counter
orders=["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course=[]
arr=[[] for _ in range(26)]
# for i in orders:
#     for j in i:
#         for k in i:
#             if j!=k:
#                 arr[ord(j)-65].append(k)
# for i in range(26):
#     tmparr=[]
#     if len(arr[i]) != 0 :
#         tmparr=Counter(arr[i]).most_common(1)
#         arr[i]=[chr(i+65),tmparr[0][0],0]
#         for j in orders:
#             if arr[i][0] in j and arr[i][1] in j:
#                 arr[i][2] += 1

print(arr)