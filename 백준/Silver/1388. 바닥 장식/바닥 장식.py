import sys
input = sys.stdin.readline



n, m = map(int, input().split())
maze = [list(input().rstrip()) for _ in range(n)]
cnt = 0

def width(cnt):
    for i in range(n):
        tmp = 0
        for j in range(m):
            if maze[i][j] == '-':
                tmp = 1
            else:
                h = height(i, j, 0)
                if h: cnt += 1
                if tmp: cnt += 1
                tmp = 0
        if tmp: cnt += 1
        tmp = 0
    return cnt
def height(x, y, tg):
    if x < 0 or x >= n or y < 0 or y >= m: return tg
    if maze[x][y] == '|':
        maze[x][y] = '*'
        tg =1
        height(x-1, y, 1)
        height(x+1, y, 1)
    return tg

cnt = width(cnt)
print(cnt)