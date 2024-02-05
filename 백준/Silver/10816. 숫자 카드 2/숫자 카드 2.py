n = int(input())
c1 = list(map(int, input().split()))
cards = {}
for i in c1:
    if i in cards: cards[i] += 1
    else: cards[i] = 1
m = int(input())
c2 = list(map(int, input().split()))
for i in c2:
    if i in cards: print(cards[i], end=' ')
    else: print(0, end=' ')