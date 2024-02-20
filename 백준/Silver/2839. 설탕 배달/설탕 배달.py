import sys
input = sys.stdin.readline

n = int(input())

def sol():
    if not n%5: return n//5
    else:
        tmp = n
        th = 0
        while tmp > 3:
            tmp -= 3
            th += 1
            if not tmp % 5:
                return tmp//5+th
        if not n%3: return n//3
        else: return -1
print(sol())