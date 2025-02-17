from collections import deque
import sys

#BFS
def BFS():

    global M,N,H
    
    # 시작점 설정(이문제는 시작점이 여러개)
    deques = deque((index))# z,y,x

    while deques:
        
        ch = deques.popleft()

        for i in range(6):
                
            ch_x,ch_y,ch_z = position[i][2]+ch[2],position[i][1] + ch[1],position[i][0] + ch[0]
            
            # 좌표가 초과하는 지 확인
            if (0 <= ch_x < M )and (0 <= ch_y < N ) and (0<= ch_z < H):

                value = ch_list[ch[0]][ch[1]][ch[2]]

                # 지금 내가 가는 곳이 좀더 빠른 시일에 전파가 가능 한지 또는 안간 곳인지 확인.
                if (ch_list[ch_z][ch_y][ch_x]) == 0 or ( (value+1) < ch_list[ch_z][ch_y][ch_x]):
                    #추가
                    deques.append((ch_z,ch_y,ch_x))
                    # 몇칠 걸리는지 갱신
                    ch_list[ch_z][ch_y][ch_x] = value + 1
                        
#메인함수

# 이동할 좌표가 index 초과가 안나는지 확인하기위해 변수 생성
position = [[0,0,1],[0,0,-1],[0,1,0],[0,-1,0],[1,0,0],[-1,0,0]]
ans = True
M,N,H = map(int,sys.stdin.readline().split()) # x,y,z

# 3차원 좌표생성
lists = [[list(map(int,sys.stdin.readline().split())) for i in range(N)] for j in range(H)]

ch_list = lists
index = []
# 삼중 for문을 돌려서 익은 토마토 찾기
for i in range(H):
    for j in range(N):
        for k in range(M):

            if lists[i][j][k] == 1:
                index.append((i,j,k))

#함수 실행
BFS()

#출력
for i in ch_list:
    for j in i:
        if 0 in j:
            print(-1)
            ans = False
            break

    if ans == False:
        break
else:
    print(max(max(max(j) for j in i) for i in ch_list)-1)
