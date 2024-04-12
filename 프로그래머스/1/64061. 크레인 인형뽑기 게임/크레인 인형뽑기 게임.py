def solution(board, moves):
    answer = 0
    st = []
    for i in moves:
        i -= 1
        for j in range(len(board)):
            if board[j][i]:
                st.append(board[j][i])
                board[j][i] = 0
                break
        if len(st) > 1 and st[-1] == st[-2]:
            st.pop()
            st.pop()
            answer += 2
    # print(st)
    # print(*board, sep='\n')
    return answer