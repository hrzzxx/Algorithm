import sys
input = sys.stdin.readline

w, h = map(int, input().split())

print(f"{w*h/2:.1f}")