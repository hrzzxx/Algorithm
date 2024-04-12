def solution(board, h, w):
    answer = 0
    dx, dy = [-1,1,0,0], [0,0,-1,1]
    color = board[h][w]
    for i in range(4):
        nx, ny = h+dx[i], w+dy[i]
        if 0<=nx<len(board) and 0<=ny<len(board) and board[nx][ny] == color: 
            answer += 1
    return answer