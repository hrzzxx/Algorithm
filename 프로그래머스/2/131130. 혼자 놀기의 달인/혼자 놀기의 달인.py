def a(cards):
    box, cur = 0,0
    for i in cards:
        if i: 
            cur = i
            break
    while cur:
        tmp = cards[cur]
        if not tmp: break
        cards[cur], cur = 0, tmp
        box += 1
    return box
def solution(cards):
    cards = [0]+cards
    box = []
    while True:
        tmp = a(cards)
        if tmp: box.append(tmp)
        else: break
    box.sort()
    if len(box) < 2: return 0
    return box.pop()*box.pop()