import sys
input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input())
    n = int(input())
    floor = {i+1:i+1 for i in range(n)}

    for i in range(1,k+1):
        for j in range(2, n+1):
            floor[j] += floor[j-1]
    print(floor[n])