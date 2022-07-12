#할머니가 외운 단어가 주어졌을 때,
# 이 전화를 걸기 위해서 필요한 최소 시간을 구하는 프로그램을 작성하시오.
a=input()
sec=0
for i in a:
    if ord(i) in range(65,68):
        sec+=3
    if ord(i) in range(68,71):
        sec+=4
    if ord(i) in range(71,74):
        sec+=5
    if ord(i) in range(74,77):
        sec+=6
    elif ord(i) in range(77,80):
        sec+=7
    elif ord(i) in range(80,84):
        sec+=8
    elif ord(i) in range(84,87):
        sec+=9
    elif ord(i) in range(87,91):
        sec+=10
print(sec)