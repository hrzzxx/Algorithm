import sys
input = sys.stdin.readline

li = [input().rstrip() for _ in range(int(input()))]
for i in li:
    tmp = i[::-1]
    if tmp in li or tmp == i:
        print(len(tmp), tmp[len(tmp)//2])
        break