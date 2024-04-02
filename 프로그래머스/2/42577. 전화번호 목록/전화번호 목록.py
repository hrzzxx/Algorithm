def solution(phone_book):
    answer = True
    phone_book.sort(key = len)
    pb = set()
    for number in phone_book:
        cur = set()
        if not pb: 
            pb.add(number)
            continue
        for i in range(1,len(number)+1):
            cur.add(number[:i])
        if pb & cur:
            return False
        else:
            pb.add(number)
    return answer