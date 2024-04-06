import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    n = str(bin(n))
    n = n[2:][::-1]
    for i,bit in enumerate(n):
        if int(bit): print(i,end=' ')
    print()