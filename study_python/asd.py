from collections import deque
import sys

#BFS
def BFS():

    global M,N
    
    deques = deque((index))

    roop_depend = []

    while deques:
        
        ch = deques.popleft()

        for i in range(4):
                
            value = ch_list[ch[0]][ch[1]]
            ch_x,ch_y = position[i][1]+ch[1],position[i][0] + ch[0]
            
            if (0 <= ch_x < M )and (0 <= ch_y < N):


                if (ch_list[ch_y][ch_x]) == 0 or (value +1 < ch_list[ch_y][ch_x]):

                    deques.append((ch_y,ch_x))  

                    ch_list[ch_y][ch_x] = value + 1
                        

position = [[0,1],[0,-1],[1,0],[-1,0]]
M,N = map(int,sys.stdin.readline().split()) # x,y

lists = [list(map(int,sys.stdin.readline().split())) for i in range(N)]

ch_list = lists

index = []
for i in range(N):
    for j in range(M):

        if lists[i][j] == 1:

            index.append([i,j])

BFS()

for i in ch_list:

    if 0 in i:
        print(-1)
        break

else:
    print(max( max(i) for i in ch_list) -1)
