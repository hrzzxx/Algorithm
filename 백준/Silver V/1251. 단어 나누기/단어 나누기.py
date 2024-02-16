import sys
input = sys.stdin.readline

word = input().rstrip()
set_ = set()
for i in range(1, len(word)):
    for j in range(1, len(word) - i):
        part1 = word[:i][::-1]
        part2 = word[i:i+j][::-1]
        part3 = word[i+j:][::-1]
        set_.add(part1 + part2 + part3)

print(min(set_))