import sys
from collections import deque

# BFS Algorisim

def BFS():
    global Column,Row
    # start position
    road = deque([[0,0,0]])# y좌표 x좌표 , 벽부슨지 확인 변수
    
    # while 문 실행
    while road:
        y,x,z = road.popleft()
        
        for i in range(4):
            
            ch_y,ch_x= go_road[i][0] + y,go_road[i][1] + x
            
            if 0 <= ch_y < Column and 0 <= ch_x < Row:
                
                #만약 벽이 없는 곳이라면
                if wall_check[ch_y][ch_x][z] == float('inf') and Matrix[ch_y][ch_x] == '0':
                    road.append([ch_y,ch_x,z])
                    wall_check[ch_y][ch_x][z] = wall_check[y][x][z] + 1
                #벽이 있고 부술 수 있는 상태라면
                elif wall_check[ch_y][ch_x][1] == float('inf') and Matrix[ch_y][ch_x] == '1' and z == 0:
                    road.append([ch_y,ch_x,1])
                    wall_check[ch_y][ch_x][1] = wall_check[y][x][z] + 1
                    
Column,Row = map(int,sys.stdin.readline().split())

go_road = [[0,1],[0,-1],[1,0],[-1,0]]

# Matrix imformation in Column and Row
Matrix = [(list(sys.stdin.readline())) for i in range(Column)]

# 최소거리 저장 리스트 
wall_check = [[[float('inf')]* 2 for j in range(Row)] for i in range(Column)]
wall_check[0][0][0] = 1

BFS()

ans = min(wall_check[Column-1][Row-1])
print(ans if ans != float('inf') else -1)