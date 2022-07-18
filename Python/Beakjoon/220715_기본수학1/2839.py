import sys
import math

A, B, V = map(int, sys.stdin.readline().split()) 
x = (V - A)/(A - B)    # x(A-B) + A => V
print(math.ceil(x) + 1 )
