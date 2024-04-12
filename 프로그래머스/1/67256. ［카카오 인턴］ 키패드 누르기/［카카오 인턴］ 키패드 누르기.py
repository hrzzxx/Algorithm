def solution(numbers, hand):
    answer = ''
    left_num, right_num = [1,4,7, 10],[3,6,9, 12]
    left, right = 10,12
    for i in numbers:
        if i == 0: i = 11
        if i in left_num: 
            answer += 'L'
            left = i
        elif i in right_num: 
            answer += 'R'
            right = i
        else:
            l, r = abs(i//3-(left-1)//3), abs(i//3 - (right-1)//3)
            if left in left_num: l += 1
            if right in right_num: r += 1
            if l == r:
                if hand == 'left': 
                    answer += 'L'
                    left = i
                else:
                    answer += 'R'
                    right = i
            elif l < r:
                answer += 'L'
                left = i
            else:
                answer += 'R'
                right = i
    return answer