cards = {}
for _ in range(int(input())):
    i = int(input())
    if i in cards: cards[i] += 1
    else: cards[i] = 1
cards = sorted(cards.items(), key=lambda x:(-x[1], x[0]))
print(cards[0][0])