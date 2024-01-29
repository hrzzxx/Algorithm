import sys
import itertools
input = sys.stdin.readline

l, c = map(int, input().split())
pw = list(input().rstrip().split())
pw.sort()
vowel = list('aeiou')
for p in list(itertools.combinations(pw, l)):
    cnt = 0
    for i in p:
        if i in vowel: cnt += 1
    if cnt >= 1 and cnt <= l-2 : print(''.join(p))